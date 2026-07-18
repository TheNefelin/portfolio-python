from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.models import Technology


async def count(db: AsyncSession, search: str = "") -> int:
  stmt = select(func.count(Technology.id_technology))
  if search:
    stmt = stmt.where(Technology.name.ilike(f"%{search}%"))
  result = await db.execute(stmt)
  return result.scalar_one()


async def get_all(db: AsyncSession, page: int = 1, limit: int = 20, search: str = "") -> list[Technology]:
  offset = (page - 1) * limit
  stmt = select(Technology).order_by(Technology.name.asc()).offset(offset).limit(limit)
  if search:
    stmt = stmt.where(Technology.name.ilike(f"%{search}%"))
  result = await db.execute(stmt)
  return list(result.scalars().all())


async def get_by_id(db: AsyncSession, id: int) -> Technology | None:
  stmt = select(Technology).where(Technology.id_technology == id)
  result = await db.execute(stmt)
  return result.scalar_one_or_none()


async def exists_by_name(db: AsyncSession, name: str, exclude_id: int | None = None) -> bool:
  stmt = select(Technology).where(Technology.name.ilike(name.strip()))
  if exclude_id is not None:
    stmt = stmt.where(Technology.id_technology != exclude_id)
  result = await db.execute(stmt)
  return result.scalar_one_or_none() is not None


async def create(db: AsyncSession, data: dict) -> Technology:
  entity = Technology(**data)
  db.add(entity)
  await db.commit()
  await db.refresh(entity)
  return entity


async def update(db: AsyncSession, entity: Technology, data: dict) -> Technology:
  for key, value in data.items():
    setattr(entity, key, value)
  await db.commit()
  await db.refresh(entity)
  return entity


async def delete(db: AsyncSession, entity: Technology) -> None:
  await db.delete(entity)
  await db.commit()
