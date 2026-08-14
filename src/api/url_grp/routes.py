from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.core.database import get_db
from src.core.dependencies import verify_api_key
from src.schemas import dtos

from . import service

router = APIRouter(prefix="/url-grp", tags=["url-grp"], dependencies=[Depends(verify_api_key)])


@router.get("/pagination", response_model=dtos.PaginationResponse[dtos.UrlGrpResponse], status_code=HTTP_200_OK)
async def get_all_pagination(
  params: Annotated[dtos.PaginationRequest, Depends()],
  db: AsyncSession = Depends(get_db),
):
  return await service.get_all(db, params.page, params.limit, params.search)


@router.get("/", response_model=list[dtos.UrlGrpResponse], status_code=HTTP_200_OK)
async def get_all(db: AsyncSession = Depends(get_db)):
  return await service.get_all_without_pagination(db)


@router.get("/detail", response_model=list[dtos.UrlGrpDetailResponse], status_code=HTTP_200_OK)
async def get_all_detail(db: AsyncSession = Depends(get_db)):
  return await service.get_all_with_urls(db)


@router.get("/{id}", response_model=dtos.UrlGrpResponse, status_code=HTTP_200_OK)
async def get_by_id(id: int, db: AsyncSession = Depends(get_db)):
  return await service.get_by_id(db, id)


@router.post("/", response_model=dtos.UrlGrpResponse, status_code=HTTP_201_CREATED)
async def create(data: dtos.UrlGrpRequest, db: AsyncSession = Depends(get_db)):
  return await service.create(db, data)


@router.put("/{id}", response_model=dtos.UrlGrpResponse, status_code=HTTP_200_OK)
async def update(id: int, data: dtos.UrlGrpRequest, db: AsyncSession = Depends(get_db)):
  return await service.update(db, id, data)


@router.delete("/{id}", status_code=HTTP_204_NO_CONTENT)
async def delete(id: int, db: AsyncSession = Depends(get_db)):
  await service.delete(db, id)