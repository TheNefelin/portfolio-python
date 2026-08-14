from sqlalchemy.ext.asyncio import AsyncSession

from src.core import image as image_service
from src.core.exceptions import DuplicateNameError, NotFoundError
from src.schemas import dtos

from . import repository

PATH = "technology"


async def get_all(db: AsyncSession, page: int = 1, limit: int = 20, search: str = "") -> dtos.PaginationResponse[dtos.TechnologyResponse]:
  total = await repository.count(db, search)
  entities = await repository.get_all(db, page, limit, search)
  items = [dtos.TechnologyResponse.model_validate(e) for e in entities]
  return dtos.PaginationResponse(page=page, limit=limit, total=total, items=items)


async def get_by_id(db: AsyncSession, id: int) -> dtos.TechnologyResponse:
  entity = await repository.get_by_id(db, id)
  if not entity:
    raise NotFoundError("Technology")
  return dtos.TechnologyResponse.model_validate(entity)


async def create(db: AsyncSession, data: dtos.TechnologyRequest) -> dtos.TechnologyResponse:
  if await repository.exists_by_name(db, data.name):
    raise DuplicateNameError(data.name)
  entity = await repository.create(db, data.model_dump())
  return dtos.TechnologyResponse.model_validate(entity)


async def update(db: AsyncSession, id: int, data: dtos.TechnologyRequest) -> dtos.TechnologyResponse:
  entity = await repository.get_by_id(db, id)
  if not entity:
    raise NotFoundError("Technology")
  if await repository.exists_by_name(db, data.name, exclude_id=id):
    raise DuplicateNameError(data.name)
  entity = await repository.update(db, entity, data.model_dump(exclude_unset=True))
  return dtos.TechnologyResponse.model_validate(entity)


async def delete(db: AsyncSession, id: int) -> None:
  entity = await repository.get_by_id(db, id)
  if not entity:
    raise NotFoundError("Technology")
  if entity.img_url:
    image_service.delete_image_by_url(entity.img_url)
  await repository.delete(db, entity)


async def upload_image(db: AsyncSession, id: int, file_bytes: bytes) -> dtos.TechnologyResponse:
  entity = await repository.get_by_id(db, id)
  if not entity:
    raise NotFoundError("Technology")
  if entity.img_url:
    image_service.delete_image_by_url(entity.img_url)
  url = image_service.upload_image_1_1(PATH, file_bytes)
  entity = await repository.update(db, entity, {"img_url": url})
  return dtos.TechnologyResponse.model_validate(entity)


async def delete_image(db: AsyncSession, id: int) -> None:
  entity = await repository.get_by_id(db, id)
  if not entity:
    raise NotFoundError("Technology")
  if entity.img_url:
    image_service.delete_image_by_url(entity.img_url)
  await repository.update(db, entity, {"img_url": None})