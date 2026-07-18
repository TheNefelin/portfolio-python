import os
import time
import uuid

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
from starlette.responses import FileResponse, JSONResponse

from src.core.config import settings
from src.core.exceptions import AppError
from src.core.limiter import limiter
from src.core.logger import logger, set_request_id

from src.api.language.routes import router as language_router
from src.api.technology.routes import router as technology_router
from src.api.project.routes import router as project_router
from src.api.url_grp.routes import router as urlgrp_router
from src.api.url.routes import router as url_router

start_time = time.time()

app = FastAPI(title="Portfolio API", description="In development", version="1.0")
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.middleware("http")
async def log_requests(request: Request, call_next):
  request_id = str(uuid.uuid4())
  set_request_id(request_id)
  start = time.time()
  response = await call_next(request)
  duration = round((time.time() - start) * 1000, 2)
  logger.info("%s %s", request.method, request.url.path, extra={
    "props": {
      "method": request.method,
      "path": request.url.path,
      "status_code": response.status_code,
      "duration_ms": duration,
    }
  })
  return response


@app.exception_handler(AppError)
async def app_error_handler(request: Request, exc: AppError):
  logger.warning("AppError: %s", exc.message, extra={
    "props": {"status_code": exc.status_code}
  })
  return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.exception_handler(Exception)
async def generic_error_handler(request: Request, exc: Exception):
  logger.error("Unhandled exception", exc_info=exc, extra={
    "props": {"status_code": 500}
  })
  return JSONResponse(status_code=500, content={"detail": "Internal server error"})


app.add_middleware(
  CORSMiddleware,
  allow_origins=settings.cors_origins_list,
  allow_credentials=True,
  allow_methods=["GET", "POST", "PUT", "DELETE"],
  allow_headers=["*"],
)

BASE_DIR = os.getcwd()
STATIC_PATH = os.path.join(BASE_DIR, "static")

app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
  return FileResponse(os.path.join(STATIC_PATH, "favicon.ico"))


@app.get("/health")
@limiter.exempt
async def health():
  return {
    "status": "Api Running",
    "swagger": "/docs",
    "uptime_seconds": round(time.time() - start_time, 2),
  }


app.include_router(language_router, prefix="/api")
app.include_router(technology_router, prefix="/api")
app.include_router(project_router, prefix="/api")
app.include_router(urlgrp_router, prefix="/api")
app.include_router(url_router, prefix="/api")
