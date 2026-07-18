import pytest
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.pool import NullPool

from src.core.config import settings
from src.core.database import Base, get_db
from src.core.dependencies import verify_api_key
from src.main import app
from src.models.models import Language, Project, ProjectLanguage, ProjectTechnology, Technology, Url, UrlGrp


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


@pytest.fixture
async def setup_db():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)
  yield
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
async def db(setup_db):
  async with TestingSessionLocal() as session:
    await _clean_tables(session)
    yield session


@pytest.fixture
async def client(db):
  async def override_get_db():
    yield db

  async def override_verify_api_key():
    return True

  app.dependency_overrides[get_db] = override_get_db
  app.dependency_overrides[verify_api_key] = override_verify_api_key
  async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
    yield ac
  app.dependency_overrides.clear()
