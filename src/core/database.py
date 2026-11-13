from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base

from src.core.config import settings

engine = create_async_engine(
  settings.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"),
  echo=settings.DEBUG,
  pool_pre_ping=True,
)

AsyncSessionLocal = async_sessionmaker(
  autocommit=False,
  autoflush=False,
  bind=engine,
  class_=AsyncSession,
)

Base = declarative_base()


async def get_db():
  async with AsyncSessionLocal() as session:
    try:
      yield session
      await session.commit()
    except Exception:
      await session.rollback()
      raise
