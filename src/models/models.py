from datetime import datetime
from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.database import Base


class Language(Base):
  __tablename__ = "pf_languages"

  id_language: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
  img_url: Mapped[str | None] = mapped_column(String(256), nullable=True)
  is_enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
  created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

  projects: Mapped[list["Project"]] = relationship(
    secondary="pf_pro_lang", back_populates="languages"
  )


class Technology(Base):
  __tablename__ = "pf_technologies"

  id_technology: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
  img_url: Mapped[str | None] = mapped_column(String(256), nullable=True)
  is_enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
  created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

  projects: Mapped[list["Project"]] = relationship(
    secondary="pf_pro_tech", back_populates="technologies"
  )


class Project(Base):
  __tablename__ = "pf_projects"

  id_project: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
  description: Mapped[str | None] = mapped_column(Text, nullable=True)
  img_url: Mapped[str | None] = mapped_column(String(256), nullable=True)
  repo_url: Mapped[str | None] = mapped_column(String(512), nullable=True)
  app_url: Mapped[str | None] = mapped_column(String(512), nullable=True)
  is_enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
  created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

  languages: Mapped[list["Language"]] = relationship(
    secondary="pf_pro_lang", back_populates="projects"
  )
  technologies: Mapped[list["Technology"]] = relationship(
    secondary="pf_pro_tech", back_populates="projects"
  )


class ProjectLanguage(Base):
  __tablename__ = "pf_pro_lang"

  id_project: Mapped[int] = mapped_column(Integer, ForeignKey("pf_projects.id_project", ondelete="RESTRICT"), primary_key=True)
  id_language: Mapped[int] = mapped_column(Integer, ForeignKey("pf_languages.id_language", ondelete="RESTRICT"), primary_key=True)


class ProjectTechnology(Base):
  __tablename__ = "pf_pro_tech"

  id_project: Mapped[int] = mapped_column(Integer, ForeignKey("pf_projects.id_project", ondelete="RESTRICT"), primary_key=True)
  id_technology: Mapped[int] = mapped_column(Integer, ForeignKey("pf_technologies.id_technology", ondelete="RESTRICT"), primary_key=True)


class UrlGrp(Base):
  __tablename__ = "pf_urlgrp"

  id_urlgrp: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
  is_enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
  created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

  urls: Mapped[list["Url"]] = relationship(back_populates="urlgrp")


class Url(Base):
  __tablename__ = "pf_url"

  id_url: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
  name: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
  link: Mapped[str] = mapped_column(String(512), nullable=False)
  is_enabled: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
  id_urlgrp: Mapped[int] = mapped_column(Integer, ForeignKey("pf_urlgrp.id_urlgrp", ondelete="RESTRICT"), nullable=False)
  created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
  updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

  urlgrp: Mapped["UrlGrp"] = relationship(back_populates="urls")
