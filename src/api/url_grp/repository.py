from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.models.models import Url, UrlGrp


async def count(db: AsyncSession, search: str = "") -> int:
  stmt = select(func.count(UrlGrp.id_urlgrp))
  if search:
    stmt = stmt.where(UrlGrp.name.ilike(f"%{search}%"))
  result = await db.execute(stmt)
  return result.scalar_one()


async def get_all(db: AsyncSession, page: int = 1, limit: int = 20, search: str = "") -> list[UrlGrp]:
  offset = (page - 1) * limit
  stmt = select(UrlGrp).order_by(UrlGrp.id_urlgrp.asc()).offset(offset).limit(limit)
  if search:
    stmt = stmt.where(UrlGrp.name.ilike(f"%{search}%"))
  result = await db.execute(stmt)
  return list(result.scalars().all())


async def get_all_without_pagination(db: AsyncSession) -> list[UrlGrp]:
  stmt = select(UrlGrp).order_by(UrlGrp.name.asc())
  result = await db.execute(stmt)
  return list(result.scalars().all())


async def get_all_with_urls(db: AsyncSession) -> list[UrlGrp]:
  stmt = select(UrlGrp).options(joinedload(UrlGrp.urls)).order_by(UrlGrp.name.asc())
  result = await db.execute(stmt)
  return list(result.unique().scalars().all())


async def get_by_id(db: AsyncSession, id: int) -> UrlGrp | None:
  stmt = select(UrlGrp).where(UrlGrp.id_urlgrp == id)
  result = await db.execute(stmt)
  return result.scalar_one_or_none()


async def exists_by_name(db: AsyncSession, name: str, exclude_id: int | None = None) -> bool:
  stmt = select(UrlGrp).where(UrlGrp.name.ilike(name.strip()))
  if exclude_id is not None:
    stmt = stmt.where(UrlGrp.id_urlgrp != exclude_id)
  result = await db.execute(stmt)
  return result.scalar_one_or_none() is not None


async def create(db: AsyncSession, data: dict) -> UrlGrp:
  entity = UrlGrp(**data)
  db.add(entity)
  await db.commit()
  await db.refresh(entity)
  return entity


async def update(db: AsyncSession, entity: UrlGrp, data: dict) -> UrlGrp:
  for key, value in data.items():
    setattr(entity, key, value)
  await db.commit()
  await db.refresh(entity)
  return entity


async def delete(db: AsyncSession, entity: UrlGrp) -> None:
  await db.delete(entity)
  await db.commit()
