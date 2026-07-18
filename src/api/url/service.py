from sqlalchemy.ext.asyncio import AsyncSession

from src.core.exceptions import DuplicateNameError
from src.schemas import dtos

from . import repository


async def get_all(db: AsyncSession, page: int = 1, limit: int = 20, search: str = "", id_urlgrp: int | None = None) -> dtos.PaginationResponse[dtos.UrlDetailResponse]:
  total = await repository.count(db, search, id_urlgrp)
  entities = await repository.get_all(db, page, limit, search, id_urlgrp)
  items = []
  for e in entities:
    data = dtos.UrlResponse.model_validate(e).model_dump()
    data["urlgrp_name"] = e.urlgrp.name if e.urlgrp else ""
    items.append(dtos.UrlDetailResponse(**data))
  return dtos.PaginationResponse(page=page, limit=limit, total=total, items=items)


async def get_by_id(db: AsyncSession, id: int) -> dtos.UrlResponse | None:
  entity = await repository.get_by_id(db, id)
  if not entity:
    return None
  return dtos.UrlResponse.model_validate(entity)


async def create(db: AsyncSession, data: dtos.UrlRequest) -> dtos.UrlResponse:
  if await repository.exists_by_name(db, data.name):
    raise DuplicateNameError(data.name)
  entity = await repository.create(db, data.model_dump())
  return dtos.UrlResponse.model_validate(entity)


async def update(db: AsyncSession, id: int, data: dtos.UrlRequest) -> dtos.UrlResponse | None:
  entity = await repository.get_by_id(db, id)
  if not entity:
    return None
  if await repository.exists_by_name(db, data.name, exclude_id=id):
    raise DuplicateNameError(data.name)
  entity = await repository.update(db, entity, data.model_dump(exclude_unset=True))
  return dtos.UrlResponse.model_validate(entity)


async def delete(db: AsyncSession, id: int) -> bool:
  entity = await repository.get_by_id(db, id)
  if not entity:
    return False
  await repository.delete(db, entity)
  return True
