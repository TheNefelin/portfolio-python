from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.project_language import repository as pro_lang_repo
from src.api.project_technology import repository as pro_tech_repo
from src.core import image as image_service
from src.core.exceptions import DuplicateNameError
from src.schemas import dtos

from . import repository

PATH = "project"


async def get_all(db: AsyncSession, page: int = 1, limit: int = 20, search: str = "") -> dtos.PaginationResponse[dtos.ProjectResponse]:
  total = await repository.count(db, search)
  entities = await repository.get_all(db, page, limit, search)
  items = [dtos.ProjectResponse.model_validate(e) for e in entities]
  return dtos.PaginationResponse(page=page, limit=limit, total=total, items=items)


async def get_by_id(db: AsyncSession, id: int) -> dtos.ProjectResponse | None:
  entity = await repository.get_by_id(db, id)
  if not entity:
    return None
  return dtos.ProjectResponse.model_validate(entity)


async def create(db: AsyncSession, data: dtos.ProjectRequest) -> dtos.ProjectResponse:
  if await repository.exists_by_name(db, data.name):
    raise DuplicateNameError(data.name)
  dump = data.model_dump(exclude={"language_ids", "technology_ids"})
  entity = await repository.create(db, dump)
  project_id = entity.id_project
  await pro_lang_repo.create_by_project(db, project_id, data.language_ids)
  await pro_tech_repo.create_by_project(db, project_id, data.technology_ids)
  return await get_by_id(db, project_id)


async def update(db: AsyncSession, id: int, data: dtos.ProjectRequest) -> dtos.ProjectResponse | None:
  entity = await repository.get_by_id(db, id)
  if not entity:
    return None
  if await repository.exists_by_name(db, data.name, exclude_id=id):
    raise DuplicateNameError(data.name)
  dump = data.model_dump(exclude_unset=True, exclude={"language_ids", "technology_ids"})
  await repository.update(db, entity, dump)
  await pro_lang_repo.delete_by_project(db, id)
  await pro_lang_repo.create_by_project(db, id, data.language_ids)
  await pro_tech_repo.delete_by_project(db, id)
  await pro_tech_repo.create_by_project(db, id, data.technology_ids)
  return await get_by_id(db, id)


async def delete(db: AsyncSession, id: int) -> bool:
  entity = await repository.get_by_id(db, id)
  if not entity:
    return False
  if entity.img_url:
    image_service.delete_image_by_url(entity.img_url)
  await repository.delete(db, entity)
  return True


async def upload_image(db: AsyncSession, id: int, file: UploadFile) -> dtos.ProjectResponse | None:
  entity = await repository.get_by_id(db, id)
  if not entity:
    return None
  if entity.img_url:
    image_service.delete_image_by_url(entity.img_url)
  url = image_service.upload_image_16_9(PATH, file)
  await repository.update(db, entity, {"img_url": url})
  return await get_by_id(db, id)


async def delete_image(db: AsyncSession, id: int) -> bool:
  entity = await repository.get_by_id(db, id)
  if not entity:
    return False
  if entity.img_url:
    image_service.delete_image_by_url(entity.img_url)
  await repository.update(db, entity, {"img_url": None})
  return True
