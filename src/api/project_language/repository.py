from sqlalchemy import delete as sqla_delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.models import ProjectLanguage


async def create_by_project(db: AsyncSession, id_project: int, ids: list[int]) -> None:
  if not ids:
    return
  await db.execute(
    insert(ProjectLanguage),
    [{"id_project": id_project, "id_language": lid} for lid in ids],
  )
  await db.commit()


async def delete_by_project(db: AsyncSession, id_project: int) -> None:
  stmt = sqla_delete(ProjectLanguage).where(ProjectLanguage.id_project == id_project)
  await db.execute(stmt)
  await db.commit()


async def delete(db: AsyncSession, id_project: int, id_language: int) -> bool:
  stmt = (
    sqla_delete(ProjectLanguage)
    .where(
      ProjectLanguage.id_project == id_project,
      ProjectLanguage.id_language == id_language,
    )
  )
  result = await db.execute(stmt)
  await db.commit()
  return result.rowcount > 0
