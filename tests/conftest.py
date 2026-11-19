import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import NullPool

from src.core.config import settings
from src.core.database import Base, get_db
from src.core.dependencies import verify_api_key
from src.core.security import require_admin
from src.main import app
from src.models.auth_models import Base as AuthBase
from src.models.models import Language, Project, ProjectLanguage, ProjectTechnology, Technology, Url, UrlGrp
from src.models.auth_models import UserRole, UserStatus, AuthProvider


test_db_url = settings.TEST_DATABASE_URL or settings.DATABASE_URL
engine = create_async_engine(test_db_url, poolclass=NullPool)
TestingSessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)


async def _clean_tables(session: AsyncSession):
  await session.execute(Url.__table__.delete())
  await session.execute(ProjectLanguage.__table__.delete())
  await session.execute(ProjectTechnology.__table__.delete())
  await session.execute(UrlGrp.__table__.delete())
  await session.execute(Project.__table__.delete())
  await session.execute(Language.__table__.delete())
  await session.execute(Technology.__table__.delete())
  # Auth tables: clean users and sessions (roles/status/providers are seeded)
  from src.models.auth_models import User, UserIdentity, UserSession
  await session.execute(UserSession.__table__.delete())
  await session.execute(UserIdentity.__table__.delete())
  await session.execute(User.__table__.delete())


@pytest.fixture
async def setup_db():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
    await conn.run_sync(AuthBase.metadata.create_all)
  yield
  async with engine.begin() as conn:
    # Drop in dependency order with CASCADE to avoid FK constraint errors
    from sqlalchemy import text
    # Auth tables (dependents first)
    for tbl in ["user_sessions", "user_identities", "user_mfa", "user_recovery_codes", "users", "user_roles", "user_status", "auth_providers"]:
      await conn.execute(text(f"DROP TABLE IF EXISTS {tbl} CASCADE"))
    # Portfolio tables (dependents first)
    for tbl in ["pf_pro_lang", "pf_pro_tech", "pf_url", "pf_projects", "pf_urlgrp", "pf_languages", "pf_technologies"]:
      await conn.execute(text(f"DROP TABLE IF EXISTS {tbl} CASCADE"))


@pytest.fixture
async def db(setup_db):
  async with TestingSessionLocal() as session:
    await _clean_tables(session)
    # Seed auth data (roles, status, providers) required by auth tests
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
  for name, display, active in [("local", "Email + Contrasena", True), ("google", "Google", True), ("github", "GitHub", False), ("apple", "Apple ID", False)]:
    existing = (await session.execute(select(AuthProvider).where(AuthProvider.name == name))).scalar_one_or_none()
    if existing is None:
      session.add(AuthProvider(name=name, display_name=display, is_active=active))
  await session.commit()


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
