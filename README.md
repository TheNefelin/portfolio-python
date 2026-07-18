# Admin Manager - API Python 3.12.x + PostgreSQL

### Deploy and run App
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
```sh
.venv\Scripts\activate
py run.py
# or 
uvicorn src.main:app --reload
```

### 1. Check Python Version & Installed Packages
```sh
py --version            # python3 --version
py -m pip list          # python3 -m pip list
py -m venv .venv        # python3 -m venv .venv
.venv\Scripts\activate  # source .venv/bin/activate
py run.py               # python3 run.py
```

### 2. Instalar dependencias
```sh
python.exe -m pip install --upgrade pip
```
```sh
pip install fastapi uvicorn[standard] sqlalchemy asyncpg greenlet python-dotenv pydantic pydantic-settings
pip install google-auth google-auth-oauthlib google-auth-httplib2
pip install pydantic[email]
pip install python-jose[cryptography]
pip install slowapi
pip install python-multipart
pip install cloudinary
```
### 3. (Opcional) Dependencias de test
```sh
pip install pytest pytest-asyncio httpx
```

Guardar dependencias:
```sh
pip freeze > requirements.txt
```

Instalar desde requirements:
```sh
pip install -r requirements.txt
```

### 4. Configurar variables de entorno
Crear archivo `.env` basado en `.env_demo`:
```sh
cp .env_example .env
```

### 5. Generar SECRET_KEY
```sh
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

---

## Tests

```sh
pytest tests/ -v
```

---

## Arquitectura

```
portfolio-python/
├── src/
│   ├── main.py                 → FastAPI app, CORS, middlewares, routers
│   ├── core/
│   │   ├── config.py           → Pydantic settings (env vars)
│   │   ├── database.py         → SQLAlchemy engine + async session
│   │   ├── dependencies.py     → DI: get_db, verify_api_key
│   │   ├── exceptions.py       → AppError base
│   │   ├── limiter.py          → slowapi rate limiter
│   │   ├── logger.py           → Logging estructurado con request_id
│   │   ├── cloudinary.py       → Cloudinary client
│   │   └── image.py            → Image processing helpers
│   ├── models/
│   │   └── models.py           → SQLAlchemy ORM entities
│   ├── schemas/
│   │   └── dtos.py             → Pydantic request/response DTOs
│   └── api/
│       ├── language/           → routes, service, repository
│       ├── technology/         → routes, service, repository
│       ├── project/            → routes, service, repository
│       ├── url_grp/            → routes, service, repository
│       └── url/                → routes, service, repository
├── tests/                      → Pytest + TestClient async
├── pytest.ini
├── run.py
└── vercel.json
```

| Capa | Tecnología |
|------|-----------|
| **Framework** | FastAPI + Uvicorn |
| **ORM** | SQLAlchemy 2.0 (async) + asyncpg |
| **DB** | PostgreSQL 16 |
| **Auth** | API Key via `X-API-Key` header |
| **Rate Limiting** | slowapi |
| **Image Hosting** | Cloudinary |
| **Testing** | pytest + pytest-asyncio + httpx

