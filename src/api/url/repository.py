from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.models.models import Url, UrlGrp


async def count(db: AsyncSession, search: str = "", id_urlgrp: int | None = None) -> int:
  stmt = select(func.count(Url.id_url))
  filters = []
  if search:
    filters.append(Url.name.ilike(f"%{search}%"))
  if id_urlgrp is not None:
    filters.append(Url.id_urlgrp == id_urlgrp)
  if filters:
    stmt = stmt.where(*filters)
  result = await db.execute(stmt)
  return result.scalar_one()


async def get_all(db: AsyncSession, page: int = 1, limit: int = 20, search: str = "", id_urlgrp: int | None = None) -> list[Url]:
  offset = (page - 1) * limit
  stmt = (
    select(Url)
    .options(joinedload(Url.urlgrp).load_only(UrlGrp.name))
    .order_by(Url.name.asc())
    .offset(offset)
    .limit(limit)
  )
  filters = []
  if search:
    filters.append(Url.name.ilike(f"%{search}%"))
  if id_urlgrp is not None:
    filters.append(Url.id_urlgrp == id_urlgrp)
  if filters:
    stmt = stmt.where(*filters)
  result = await db.execute(stmt)
  return list(result.unique().scalars().all())


async def get_by_id(db: AsyncSession, id: int) -> Url | None:
  stmt = select(Url).where(Url.id_url == id)
  result = await db.execute(stmt)
  return result.scalar_one_or_none()


async def exists_by_name(db: AsyncSession, name: str, exclude_id: int | None = None) -> bool:
  stmt = select(Url).where(Url.name.ilike(name.strip()))
  if exclude_id is not None:
    stmt = stmt.where(Url.id_url != exclude_id)
  result = await db.execute(stmt)
  return result.scalar_one_or_none() is not None


async def create(db: AsyncSession, data: dict) -> Url:
  entity = Url(**data)
  db.add(entity)
  await db.commit()
  await db.refresh(entity)
  return entity


async def update(db: AsyncSession, entity: Url, data: dict) -> Url:
  for key, value in data.items():
    setattr(entity, key, value)
  await db.commit()
  await db.refresh(entity)
  return entity


async def delete(db: AsyncSession, entity: Url) -> None:
  await db.delete(entity)
  await db.commit()
