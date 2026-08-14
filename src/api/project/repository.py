from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from src.models.models import Language, Project, Technology


def _relations_options():
  return [
    joinedload(Project.languages).load_only(Language.id_language, Language.name, Language.img_url, Language.is_enabled),
    joinedload(Project.technologies).load_only(Technology.id_technology, Technology.name, Technology.img_url, Technology.is_enabled),
  ]


async def _resolve_languages(db: AsyncSession, ids: list[int]) -> list[Language]:
  if not ids:
    return []
  result = await db.execute(select(Language).where(Language.id_language.in_(ids)))
  return list(result.scalars().all())


async def _resolve_technologies(db: AsyncSession, ids: list[int]) -> list[Technology]:
  if not ids:
    return []
  result = await db.execute(select(Technology).where(Technology.id_technology.in_(ids)))
  return list(result.scalars().all())


async def count(db: AsyncSession, search: str = "") -> int:
  stmt = select(func.count(Project.id_project))
  if search:
    stmt = stmt.where(Project.name.ilike(f"%{search}%"))
  result = await db.execute(stmt)
  return result.scalar_one()


async def get_all(db: AsyncSession, page: int = 1, limit: int = 20, search: str = "") -> list[Project]:
  offset = (page - 1) * limit
  stmt = select(Project).options(*_relations_options()).order_by(Project.id_project.desc()).offset(offset).limit(limit)
  if search:
    stmt = stmt.where(Project.name.ilike(f"%{search}%"))
  result = await db.execute(stmt)
  return list(result.unique().scalars().all())


async def get_by_id(db: AsyncSession, id: int) -> Project | None:
  stmt = select(Project).options(*_relations_options()).where(Project.id_project == id)
  result = await db.execute(stmt)
  return result.unique().scalar_one_or_none()


async def exists_by_name(db: AsyncSession, name: str, exclude_id: int | None = None) -> bool:
  stmt = select(Project).where(Project.name.ilike(name.strip()))
  if exclude_id is not None:
    stmt = stmt.where(Project.id_project != exclude_id)
  result = await db.execute(stmt)
  return result.scalar_one_or_none() is not None


async def create(db: AsyncSession, data: dict, language_ids: list[int], technology_ids: list[int]) -> Project:
  entity = Project(**data)
  entity.languages = await _resolve_languages(db, language_ids)
  entity.technologies = await _resolve_technologies(db, technology_ids)
  db.add(entity)
  await db.flush()
  project_id = entity.id_project
  await db.commit()
  return await get_by_id(db, project_id)


async def update(db: AsyncSession, entity: Project, data: dict, language_ids: list[int], technology_ids: list[int]) -> Project:
  for key, value in data.items():
    setattr(entity, key, value)
  entity.languages = await _resolve_languages(db, language_ids)
  entity.technologies = await _resolve_technologies(db, technology_ids)
  project_id = entity.id_project
  await db.commit()
  return await get_by_id(db, project_id)


async def set_image_url(db: AsyncSession, id: int, url: str | None) -> Project:
  entity = await get_by_id(db, id)
  if not entity:
    return entity
  entity.img_url = url
  await db.commit()
  return await get_by_id(db, id)


async def delete(db: AsyncSession, entity: Project) -> None:
  await db.delete(entity)
  await db.commit()