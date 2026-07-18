from datetime import datetime
from typing import Generic, TypeVar

from pydantic import BaseModel, ConfigDict, Field

T = TypeVar("T")


class AppModel(BaseModel):
  model_config = ConfigDict(from_attributes=True)


# ── Pagination ──────────────────────────────────────────

class PaginationRequest(BaseModel):
  page: int = Field(default=1, ge=1)
  limit: int = Field(default=20, ge=1, le=100)
  search: str = Field(default="")


class PaginationResponse(BaseModel, Generic[T]):
  page: int
  limit: int
  total: int
  items: list[T]


# ── Language ────────────────────────────────────────────

class LanguageRequest(BaseModel):
  name: str = Field(min_length=1, max_length=50)
  is_enabled: bool = True


class LanguageResponse(AppModel):
  id_language: int
  name: str
  img_url: str | None = None
  is_enabled: bool


# ── Technology ──────────────────────────────────────────

class TechnologyRequest(BaseModel):
  name: str = Field(min_length=1, max_length=50)
  is_enabled: bool = True


class TechnologyResponse(AppModel):
  id_technology: int
  name: str
  img_url: str | None = None
  is_enabled: bool


# ── Project ─────────────────────────────────────────────

class ProjectRequest(BaseModel):
  name: str = Field(min_length=1, max_length=100)
  description: str | None = None
  repo_url: str | None = None
  app_url: str | None = None
  is_enabled: bool = False
  language_ids: list[int] = []
  technology_ids: list[int] = []


class ProjectResponse(AppModel):
  id_project: int
  name: str
  description: str | None = None
  img_url: str | None = None
  repo_url: str | None = None
  app_url: str | None = None
  is_enabled: bool
  created_at: datetime
  updated_at: datetime
  languages: list["LanguageResponse"] = []
  technologies: list["TechnologyResponse"] = []


# ── UrlGrp ──────────────────────────────────────────────

class UrlGrpRequest(BaseModel):
  name: str = Field(min_length=1, max_length=50)
  is_enabled: bool = True


class UrlGrpResponse(AppModel):
  id_urlgrp: int
  name: str
  is_enabled: bool


class UrlGrpDetailResponse(UrlGrpResponse):
  urls: list["UrlResponse"] = []


# ── Url ─────────────────────────────────────────────────

class UrlRequest(BaseModel):
  name: str = Field(min_length=1, max_length=100)
  link: str = Field(min_length=1, max_length=512)
  is_enabled: bool = True
  id_urlgrp: int = Field(..., gt=0)


class UrlResponse(AppModel):
  id_url: int
  name: str
  link: str
  is_enabled: bool
  id_urlgrp: int


class UrlDetailResponse(UrlResponse):
  urlgrp_name: str
