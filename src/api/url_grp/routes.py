from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.database import get_db
from src.core.dependencies import verify_api_key
from src.schemas import dtos

from . import service

router = APIRouter(
  prefix="/url-grp",
  tags=["url-grp"],
  dependencies=[Depends(verify_api_key)],
)


@router.get("/pagination", response_model=dtos.PaginationResponse[dtos.UrlGrpResponse])
async def get_all_pagination(
  page: int = Query(default=1, ge=1),
  limit: int = Query(default=20, ge=1, le=100),
  search: str = Query(default=""),
  db: AsyncSession = Depends(get_db),
):
  return await service.get_all(db, page, limit, search)


@router.get("/", response_model=list[dtos.UrlGrpResponse])
async def get_all(db: AsyncSession = Depends(get_db)):
  return await service.get_all_without_pagination(db)


@router.get("/detail", response_model=list[dtos.UrlGrpDetailResponse])
async def get_all_detail(db: AsyncSession = Depends(get_db)):
  return await service.get_all_with_urls(db)


@router.get("/{id}", response_model=dtos.UrlGrpResponse)
async def get_by_id(id: int, db: AsyncSession = Depends(get_db)):
  item = await service.get_by_id(db, id)
  if not item:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="UrlGrp not found")
  return item


@router.post("/", response_model=dtos.UrlGrpResponse, status_code=status.HTTP_201_CREATED)
async def create(data: dtos.UrlGrpRequest, db: AsyncSession = Depends(get_db)):
  return await service.create(db, data)


@router.put("/{id}", response_model=dtos.UrlGrpResponse)
async def update(id: int, data: dtos.UrlGrpRequest, db: AsyncSession = Depends(get_db)):
  item = await service.update(db, id, data)
  if not item:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="UrlGrp not found")
  return item


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: int, db: AsyncSession = Depends(get_db)):
  deleted = await service.delete(db, id)
  if not deleted:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="UrlGrp not found")
