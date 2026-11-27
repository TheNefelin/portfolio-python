import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import NullPool

from src.core.config import settings
from src.core.database import Base, get_db
from src.core.dependencies import verify_api_key
from src.core.limiter import limiter
from src.core.security import require_admin
from src.main import app
from src.models.auth_models import Base as AuthBase
from src.models.models import Language, Project, ProjectLanguage, ProjectTechnology, Technology, Url, UrlGrp
from src.models.auth_models import UserRole, UserStatus, AuthProvider


# Desactivar rate limit en tests (a nivel de modulo)
limiter.enabled = False

engine = create_async_engine(settings.TEST_DATABASE_URL, poolclass=NullPool)
TestingSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


# Solo las tablas de ESTE proyecto (prefijo pf_* + auth). Derivadas de
# postgre_schema.sql y postgre_auth.sql. El aislamiento entre proyectos lo da
# la BD dedicada, no esta lista.
TEST_TABLES = [
    "pf_pro_lang", "pf_pro_tech", "pf_url", "pf_projects", "pf_urlgrp",
    "pf_languages", "pf_technologies",
    "user_sessions", "user_identities", "user_mfa", "user_recovery_codes",
    "users", "user_roles", "user_status", "auth_providers",
]


async def _clean_tables(session: AsyncSession):
    """Vacía las tablas del proyecto entre tests (TRUNCATE + RESTART IDENTITY)."""
    from sqlalchemy import text
    await session.execute(
        text(f"TRUNCATE {', '.join(TEST_TABLES)} RESTART IDENTITY CASCADE")
    )
    await session.commit()


@pytest.fixture(scope="module")
async def setup_db():
    # Aplica el DDL real del proyecto (idempotente, CREATE TABLE IF NOT EXISTS).
    # NO hace DROP SCHEMA. La BD de tests es dedicada y desechable.
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.run_sync(AuthBase.metadata.create_all)
    yield
    # Sin teardown destructivo: la BD de tests se resetea con repopulate_db.py.


@pytest.fixture
async def db(setup_db):
    async with TestingSessionLocal() as session:
        await _clean_tables(session)
        # Seed mínimo: roles, status, providers
        await _seed_auth(session)
        yield session


async def _seed_auth(session: AsyncSession):
    from sqlalchemy import select
    # Roles
    for name, desc in [("admin", "Administrador del sistema"), ("user", "Usuario estandar")]:
        existing = (await session.execute(select(UserRole).where(UserRole.name == name))).scalar_one_or_none()
        if existing is None:
            session.add(UserRole(name=name, description=desc))
    # Status
    for name in ["activo", "inactivo", "bloqueado"]:
        existing = (await session.execute(select(UserStatus).where(UserStatus.name == name))).scalar_one_or_none()
        if existing is None:
            session.add(UserStatus(name=name))
    # Providers
    for name, display, active in [("local", "Email + Contrasena", True), ("google", "Google", True), ("github", "GitHub", True), ("apple", "Apple ID", False)]:
        existing = (await session.execute(select(AuthProvider).where(AuthProvider.name == name))).scalar_one_or_none()
        if existing is None:
            session.add(AuthProvider(name=name, display_name=display, is_active=active))
    await session.commit()


@pytest.fixture(autouse=True)
def _reset_rate_limiter():
    limiter.reset()
    yield


@pytest.fixture
async def client(db):
    async def override_get_db():
        yield db

    async def override_verify_api_key():
        return True

    async def override_require_admin():
        return {"id": "test-admin", "role": "admin", "email": "admin@test.com", "is_active": True}

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[verify_api_key] = override_verify_api_key
    app.dependency_overrides[require_admin] = override_require_admin
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()