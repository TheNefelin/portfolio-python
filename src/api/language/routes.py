from typing import Annotated
from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from src.core.database import get_db
from src.core.dependencies import verify_api_key
from src.schemas import dtos

from . import service

router = APIRouter(prefix="/language", tags=["language"], dependencies=[Depends(verify_api_key)])


@router.get("/pagination", response_model=dtos.PaginationResponse[dtos.LanguageResponse], status_code=HTTP_200_OK)
async def get_all_pagination(
  params: Annotated[dtos.PaginationRequest, Depends()],
  db: AsyncSession = Depends(get_db),
):
  return await service.get_all(db, params.page, params.limit, params.search)


@router.get("/", response_model=list[dtos.LanguageResponse], status_code=HTTP_200_OK)
async def get_all(db: AsyncSession = Depends(get_db)):
  result = await service.get_all(db, page=1, limit=100)
  return result.items


@router.get("/{id}", response_model=dtos.LanguageResponse, status_code=HTTP_200_OK)
async def get_by_id(id: int, db: AsyncSession = Depends(get_db)):
  return await service.get_by_id(db, id)


@router.post("/", response_model=dtos.LanguageResponse, status_code=HTTP_201_CREATED)
async def create(data: dtos.LanguageRequest, db: AsyncSession = Depends(get_db)):
  return await service.create(db, data)


@router.put("/{id}", response_model=dtos.LanguageResponse, status_code=HTTP_200_OK)
async def update(id: int, data: dtos.LanguageRequest, db: AsyncSession = Depends(get_db)):
  return await service.update(db, id, data)


@router.delete("/{id}", status_code=HTTP_204_NO_CONTENT)
async def delete(id: int, db: AsyncSession = Depends(get_db)):
  await service.delete(db, id)


@router.post("/{id}/upload-image", response_model=dtos.LanguageResponse, status_code=HTTP_200_OK)
async def upload_image(id: int, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
  return await service.upload_image(db, id, await file.read())


@router.delete("/{id}/image", status_code=HTTP_204_NO_CONTENT)
async def delete_image(id: int, db: AsyncSession = Depends(get_db)):
  await service.delete_image(db, id)