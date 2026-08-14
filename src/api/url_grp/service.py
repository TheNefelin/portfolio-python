from sqlalchemy.ext.asyncio import AsyncSession

from src.core.exceptions import DuplicateNameError, NotFoundError
from src.schemas import dtos

from . import repository


async def get_all(db: AsyncSession, page: int = 1, limit: int = 20, search: str = "") -> dtos.PaginationResponse[dtos.UrlGrpResponse]:
  total = await repository.count(db, search)
  entities = await repository.get_all(db, page, limit, search)
  items = [dtos.UrlGrpResponse.model_validate(e) for e in entities]
  return dtos.PaginationResponse(page=page, limit=limit, total=total, items=items)


async def get_all_without_pagination(db: AsyncSession) -> list[dtos.UrlGrpResponse]:
  entities = await repository.get_all_without_pagination(db)
  return [dtos.UrlGrpResponse.model_validate(e) for e in entities]


async def get_all_with_urls(db: AsyncSession) -> list[dtos.UrlGrpDetailResponse]:
  entities = await repository.get_all_with_urls(db)
  return [dtos.UrlGrpDetailResponse.model_validate(e) for e in entities]


async def get_by_id(db: AsyncSession, id: int) -> dtos.UrlGrpResponse:
  entity = await repository.get_by_id(db, id)
  if not entity:
    raise NotFoundError("UrlGrp")
  return dtos.UrlGrpResponse.model_validate(entity)


async def create(db: AsyncSession, data: dtos.UrlGrpRequest) -> dtos.UrlGrpResponse:
  if await repository.exists_by_name(db, data.name):
    raise DuplicateNameError(data.name)
  entity = await repository.create(db, data.model_dump())
  return dtos.UrlGrpResponse.model_validate(entity)


async def update(db: AsyncSession, id: int, data: dtos.UrlGrpRequest) -> dtos.UrlGrpResponse:
  entity = await repository.get_by_id(db, id)
  if not entity:
    raise NotFoundError("UrlGrp")
  if await repository.exists_by_name(db, data.name, exclude_id=id):
    raise DuplicateNameError(data.name)
  entity = await repository.update(db, entity, data.model_dump(exclude_unset=True))
  return dtos.UrlGrpResponse.model_validate(entity)


async def delete(db: AsyncSession, id: int) -> None:
  entity = await repository.get_by_id(db, id)
  if not entity:
    raise NotFoundError("UrlGrp")
  await repository.delete(db, entity)