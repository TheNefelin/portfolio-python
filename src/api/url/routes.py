from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.core.dependencies import verify_api_key
from src.schemas import dtos

from . import service

router = APIRouter(
  prefix="/url",
  tags=["url"],
  dependencies=[Depends(verify_api_key)],
)


@router.get("/pagination", response_model=dtos.PaginationResponse[dtos.UrlDetailResponse])
async def get_all_pagination(
  page: int = Query(default=1, ge=1),
  limit: int = Query(default=20, ge=1, le=100),
  search: str = Query(default=""),
  id_urlgrp: int = Query(default=None),
  db: AsyncSession = Depends(get_db),
):
  return await service.get_all(db, page, limit, search, id_urlgrp)


@router.get("/", response_model=list[dtos.UrlResponse])
async def get_all(db: AsyncSession = Depends(get_db)):
  result = await service.get_all(db, page=1, limit=100)
  return result.items


@router.get("/{id}", response_model=dtos.UrlResponse)
async def get_by_id(id: int, db: AsyncSession = Depends(get_db)):
  item = await service.get_by_id(db, id)
  if not item:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
  return item


@router.post("/", response_model=dtos.UrlResponse, status_code=status.HTTP_201_CREATED)
async def create(data: dtos.UrlRequest, db: AsyncSession = Depends(get_db)):
  return await service.create(db, data)


@router.put("/{id}", response_model=dtos.UrlResponse)
async def update(id: int, data: dtos.UrlRequest, db: AsyncSession = Depends(get_db)):
  item = await service.update(db, id, data)
  if not item:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
  return item


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int, db: AsyncSession = Depends(get_db)):
  deleted = await service.delete(db, id)
  if not deleted:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="URL not found")
