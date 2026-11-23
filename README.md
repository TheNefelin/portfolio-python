# Admin Manager - API Python 3.12.x + PostgreSQL

### Deploy and run App
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
```sh
.venv\Scripts\activate
python repopulate_db.py   # puebla la BD (schema + seed) usando DATABASE_URL del .env
python run.py
# or 
uvicorn src.main:app --reload
```

### 1. Check Python Version & Installed Packages
```sh
python --version            # python3 --version
python -m pip list          # python3 -m pip list
python -m venv .venv        # python3 -m venv .venv
.venv\Scripts\activate      # source .venv/bin/activate
python run.py               # python3 run.py
```

### 2. Instalar dependencias
```sh
python.exe -m pip install --upgrade pip
```
```sh
# Web framework y servidor
pip install fastapi uvicorn[standard]
# ORM y base de datos
pip install sqlalchemy asyncpg greenlet
# Configuración y validación
pip install python-dotenv pydantic pydantic-settings
# Rate limiting
pip install slowapi
# Errores estandarizados RFC 9457 (Problem Details)
pip install fastapi-problem rfc9457
# Parseo de formularios multipart (subida de archivos)
pip install python-multipart
# Almacenamiento de imágenes en Cloudinary
pip install cloudinary
# Autenticación (JWT + contraseñas hasheadas)
pip install python-jose[cryptography] pwdlib[bcrypt] bcrypt cryptography ecdsa pyasn1 pycparser rsa cffi
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
Crear archivo `.env` basado en `.env.example`:
```sh
cp .env.example .env
```

### 4.1 Configurar OAuth (opcional)

El proyecto soporta login con Google, GitHub y Apple. Solo Google y GitHub están activos por defecto; Apple está desactivado (requiere Apple Developer Program, $99/año).

**Google Sign In:**
1. Ve a [Google Cloud Console](https://console.cloud.google.com) → APIs & Services → Credentials.
2. Crea un OAuth 2.0 Client ID (tipo "Web application").
3. Añade `http://localhost:4200` y tu dominio de producción a "Authorized JavaScript origins".
4. Copia el Client ID a `GOOGLE_CLIENT_ID` en `.env`.

**GitHub OAuth:**
1. Ve a [github.com/settings/developers](https://github.com/settings/developers) → OAuth Apps → New OAuth App.
2. Rellena: Application name, Homepage URL (`http://localhost:4200`), Authorization callback URL (`http://localhost:4200/auth/github/callback`).
3. Copia Client ID y Client Secret a `GITHUB_CLIENT_ID` y `GITHUB_CLIENT_SECRET` en `.env`.

**Apple Sign In (opcional, requiere Apple Developer Program $99/año):**
1. Ve a [developer.apple.com](https://developer.apple.com) → Certificates, Identifiers & Profiles.
2. Crea un App ID con "Sign in with Apple" habilitado.
3. Crea un Services ID (este es el `APPLE_CLIENT_ID`).
4. Configura el dominio y las redirect URLs.
5. Verifica el dominio hosteando el archivo de asociación en `https://tu-dominio/.well-known/apple-developer-domain-association.txt`.
6. Copia el Services ID a `APPLE_CLIENT_ID` en `.env`.
7. Para activar: cambia `is_active` a `TRUE` en `postgre_auth.sql` para el proveedor `apple`.

### 5. Generar SECRET_KEY
```sh
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 6. Poblar / reconstruir la base de datos
`repopulate_db.py` aplica `postgre_schema.sql` (esquema) y `postgre_seed.sql` (datos iniciales) a la BD definida en `.env`:

```sh
python repopulate_db.py            # aplica schema + seed (idempotente)
python repopulate_db.py --force    # DROP + CREATE de la BD y luego aplica schema + seed
python repopulate_db.py --test     # usa TEST_DATABASE_URL en lugar de DATABASE_URL
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
│   │   ├── exceptions.py       → Errores de dominio basados en RFC 9457
│   │   ├── limiter.py          → slowapi rate limiter
│   │   ├── logger.py           → Logging estructurado con request_id
│   │   ├── cloudinary.py       → Cloudinary client
│   │   └── image.py            → Image processing helpers
│   ├── models/
│   │   └── models.py           → SQLAlchemy ORM entities
│   ├── schemas/
│   │   └── dtos.py             → Pydantic request/response DTOs
│   └── api/
│       ├── auth/               → routes, service, repository, google_service
│       ├── language/           → routes, service, repository
│       ├── technology/         → routes, service, repository
│       ├── project/            → routes, service, repository
│       ├── url_grp/            → routes, service, repository
│       └── url/                → routes, service, repository
├── tests/                      → Pytest + TestClient async
├── repopulate_db.py            → Reconstruye la BD desde los .sql
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
| **Errores** | RFC 9457 via fastapi-problem + rfc9457 |
| **Image Hosting** | Cloudinary |
| **Testing** | pytest + pytest-asyncio + httpx

