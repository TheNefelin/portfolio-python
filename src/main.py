import os
import time
import uuid

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi_problem.handler import add_exception_handler, new_exception_handler
from rfc9457 import BadRequestProblem, Problem, ServerProblem, UnprocessableProblem
from slowapi.errors import RateLimitExceeded
from starlette.responses import FileResponse, JSONResponse

from src.api.language.routes import router as language_router
from src.api.project.routes import router as project_router
from src.api.technology.routes import router as technology_router
from src.api.url.routes import router as url_router
from src.api.url_grp.routes import router as urlgrp_router
from src.core.config import settings
from src.core.limiter import limiter
from src.core.logger import logger, set_request_id

start_time = time.time()

app = FastAPI(title="Portfolio API", description="In development", version="1.0")
app.state.limiter = limiter


class RequestValidationProblem(UnprocessableProblem):
  type_ = "request-validation-failed"
  title = "Request validation error."

  def __init__(self, errors=None, **kwargs):
    super().__init__(errors=errors, **kwargs)
    self.detail = "; ".join(str(e.get("msg", "")) for e in errors) if errors else self.title


class InternalServerErrorProblem(ServerProblem):
  type_ = "internal-server-error"
  title = "Internal server error."

  def __init__(self, detail=None, **kwargs):
    super().__init__(detail="Internal server error", **kwargs)


class RateLimitProblem(BadRequestProblem):
  type_ = "rate-limit-exceeded"
  title = "Rate limit exceeded."
  status = 429


def rate_limit_handler(eh, request: Request, exc: RateLimitExceeded):
  headers = None
  if hasattr(request.state, "view_rate_limit"):
    response = request.app.state.limiter._inject_headers(JSONResponse({}), request.state.view_rate_limit)
    headers = dict(response.headers)
  return RateLimitProblem(detail=f"Rate limit exceeded: {exc.detail}", headers=headers)


def log_problem(request: Request, exc: Exception):
  if isinstance(exc, Problem) and exc.status < 500:
    logger.warning("%s: %s", exc.title, exc.detail, extra={"props": {"status_code": exc.status}})


eh = new_exception_handler(
  logger=logger,
  unhandled_wrappers={"422": RequestValidationProblem, "500": InternalServerErrorProblem},
  handlers={RateLimitExceeded: rate_limit_handler},
  pre_hooks=[log_problem],
)
add_exception_handler(app, eh)
app.add_exception_handler(RateLimitExceeded, eh)


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
