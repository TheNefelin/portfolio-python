# Desarrollo — portfolio-python

> Memoria del proyecto: decisiones y estado que deben sobrevivir a cada sesión.
> Marca el **estado** de cada decisión (`Aceptado`, `Pendiente`); lo desconocido se anota, no se inventa.
> Reemplaza el estado caducado en vez de acumular un diario de cada sesión.

## Mapa del proyecto

| Área / tema | Dónde mirar | Cuándo leerlo |
|---|---|---|
| API y rutas | `src/main.py`, `src/api/*/routes.py` | al tocar endpoints, CORS o middleware |
| Auth | `src/api/auth/` (routes, service, repository, google_service), `src/core/security.py`, `src/models/auth_models.py` | al tocar login, refresh, roles o la API key |
| Esquema de auth | `postgre_auth.sql` | al cambiar tablas de usuario |
| Lógica de negocio | `src/api/*/service.py` | al cambiar validaciones, paginación o imágenes |
| Persistencia | `src/api/*/repository.py`, `src/models/models.py` | al cambiar consultas, entidades o atomicidad |
| Contratos request/response | `src/schemas/dtos.py`, `src/schemas/auth_dtos.py` | al cambiar DTOs o paginación |
| Configuración y BD | `src/core/config.py`, `src/core/database.py`, `.env.example` | al agregar variables o cambiar la conexión |
| Errores de dominio | `src/core/exceptions.py` | al agregar o cambiar errores |
| Imágenes | `src/core/cloudinary.py`, `src/core/image.py` | al tocar subida, borrado o URLs |
| Esquema y datos | `postgre_schema.sql`, `postgre_seed.sql`, `repopulate_db.py` | al cambiar tablas, columnas o seed |
| Tests | `tests/`, `pytest.ini` | al agregar cobertura; `live` se excluye por defecto |
| Despliegue local/Vercel | `run.py`, `vercel.json`, `README.md` | al cambiar el arranque o el runtime |

## Arquitectura

API FastAPI por feature. Cada feature vive en `src/api/<feature>/` y expone `routes.py`, `service.py` y `repository.py`.

- **Flujo:** `routes → service → repository`.
- **Repository:** única capa que conoce SQLAlchemy y la única que hace commit.
- **Service:** orquesta el negocio (errores, imágenes, paginación). Lanza `NotFoundError`; nunca devuelve `None` para "no encontrado".
- **Entidades:** prefijo `pf_*` y columnas `id_<tabla>`; las tablas de auth (`users`, `user_roles`, `user_status`, `auth_providers`, `user_identities`, `user_sessions`) viven aparte, en `postgre_auth.sql`.
- **API:** los routers se montan bajo `/api`; los estáticos, bajo `/static`.
- **Auth:** `routes → service → repository`, con `google_service` validando el token de Google. Toda la API exige `X-API-Key` a nivel de router; solo `/health` y `/docs` quedan fuera.
- **Errores:** RFC 9457 (`fastapi-problem` + `rfc9457`) para respuestas uniformes.

## Decisiones

| Estado | Decisión | Motivo |
|---|---|---|
| Aceptado | Arquitectura por feature con `routes`, `service` y `repository`. | Aísla HTTP, negocio y persistencia. |
| Aceptado | El repository es la única capa que hace commit; las relaciones M:N de `project` se resuelven en un único commit. | Evita commits parciales y dependencias cruzadas entre features. |
| Aceptado | Errores de dominio con RFC 9457. | Respuestas uniformes y cliente predecible. |
| Aceptado | Imágenes en Cloudinary; la BD guarda solo la URL. | Evita binarios en la base y simplifica el borrado idempotente. |
| Aceptado | Auth con Google OAuth + JWT: access token de 15 min, refresh rotativo de 1 día, revocación y detección de reuso en `user_sessions`. Roles `admin` y `user` en `user_roles`. | Sesión sin guardar contraseñas; el refresh rotativo limita el uso de un token robado. |
| Aceptado | `google_service` valida `aud` contra `GOOGLE_CLIENT_ID` y `email_verified`; acepta `id_token` (JWT) o `access_token` opaco. | Un token emitido para otra app no debe crear sesión. |
| Aceptado | Tests con `pytest`; los casos `@pytest.mark.live` se excluyen por defecto. | Los tests base no dependen de servicios externos reales. |
| Aceptado | Contrato de auth alineado con `portfolio-angular`: la API devuelve `{access_token, refresh_token, token_type, expires_in}` y el BFF (cookies HttpOnly) consume `access_token`. `/auth/me` devuelve `UserProfile`. | El BFF gestiona la sesión; el front no accede a los tokens. |

## Estado

- API activa con los routers `language`, `technology`, `project`, `url`, `url-grp` y `auth` montados bajo `/api`.
- 62 tests en `tests/` (última corrida registrada: 62 pasan). Sin cobertura de auth.
- [ ] Confirmar si el error 400 de `POST /api/project` sigue vigente y cuál es su causa.

## Pendientes

- **Sin tests de auth:** no hay casos para `google`, `refresh`, `logout` ni para la verificación de `X-API-Key`.
- **GitHub y Apple:** `config.py` y `.env.example` declaran credenciales, pero no hay validación de esos proveedores.
- **Error 400 en `POST /api/project`:** aparcado; no crítico por ahora.

## Problemas conocidos

- El error 400 de creación de `project`.
- El contrato de auth está alineado con el front (cookies HttpOnly en el BFF).

## Deuda técnica

- `live` depende de servicios externos reales; no se ejecuta en la suite por defecto.
- `core/roles.py` documenta una validación del catálogo de roles al arrancar que no está implementada (no existe `core/startup.py`); el catálogo real está en la tabla `user_roles`.
