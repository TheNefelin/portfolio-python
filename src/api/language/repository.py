from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.models import Language


async def count(db: AsyncSession, search: str = "") -> int:
  stmt = select(func.count(Language.id_language))
  if search:
    stmt = stmt.where(Language.name.ilike(f"%{search}%"))
  result = await db.execute(stmt)
  return result.scalar_one()


async def get_all(db: AsyncSession, page: int = 1, limit: int = 20, search: str = "") -> list[Language]:
  offset = (page - 1) * limit
  stmt = select(Language).order_by(Language.name.asc()).offset(offset).limit(limit)
  if search:
    stmt = stmt.where(Language.name.ilike(f"%{search}%"))
  result = await db.execute(stmt)
  return list(result.scalars().all())


async def get_by_id(db: AsyncSession, id: int) -> Language | None:
  stmt = select(Language).where(Language.id_language == id)
  result = await db.execute(stmt)
  return result.scalar_one_or_none()


async def exists_by_name(db: AsyncSession, name: str, exclude_id: int | None = None) -> bool:
  stmt = select(Language).where(Language.name.ilike(name.strip()))
  if exclude_id is not None:
    stmt = stmt.where(Language.id_language != exclude_id)
  result = await db.execute(stmt)
  return result.scalar_one_or_none() is not None


async def create(db: AsyncSession, data: dict) -> Language:
  entity = Language(**data)
  db.add(entity)
  await db.commit()
  await db.refresh(entity)
  return entity


async def update(db: AsyncSession, entity: Language, data: dict) -> Language:
  for key, value in data.items():
    setattr(entity, key, value)
  await db.commit()
  await db.refresh(entity)
  return entity


async def delete(db: AsyncSession, entity: Language) -> None:
  await db.delete(entity)
  await db.commit()
