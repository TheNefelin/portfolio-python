# Desarrollo — portfolio-python

> Memoria del proyecto: decisiones y estado que deben sobrevivir a cada sesión.
> Marca el **estado** de cada decisión (`Aceptado`, `Propuesto`, `Pendiente`); lo desconocido se anota, no se inventa.
> Reemplaza el estado caducado en vez de acumular un diario de cada sesión.
> Empieza por el **Mapa del proyecto**: apunta a dónde mirar sin re-escanear el código.

## Mapa del proyecto

| Área / tema | Dónde mirar | Cuándo leerlo |
|---|---|---|
| API y rutas | `src/main.py`, `src/api/*/routes.py` | al tocar endpoints, CORS, middleware o RFC 9457 |
| Auth | `src/api/auth/` (WIP, sin montar), `src/core/security.py` y `src/api/users/` (no existen) | al retomar auth; hoy no se toca |
| Lógica de negocio | `src/api/*/service.py` | al cambiar validaciones, paginación o imágenes |
| Persistencia | `src/api/*/repository.py`, `src/models/models.py` | al cambiar consultas, entidades o atomicidad |
| Contratos request/response | `src/schemas/dtos.py` | al cambiar DTOs o paginación |
| Configuración y BD | `src/core/config.py`, `src/core/database.py`, `.env_demo` | al agregar variables o cambiar la conexión |
| Errores de dominio | `src/core/exceptions.py` | al agregar o cambiar errores |
| Imágenes | `src/core/cloudinary.py`, `src/core/image.py` | al tocar subida, borrado o URLs |
| Esquema y datos iniciales | `postgre_schema.sql`, `postgre_seed.sql`, `repopulate_db.py` | al cambiar tablas, columnas o seed |
| Tests | `tests/`, `pytest.ini` | al agregar cobertura; `live` queda excluido por defecto |
| Despliegue local/Vercel | `run.py`, `vercel.json`, `README.md` | al cambiar el arranque o el runtime |

## Arquitectura

API FastAPI organizada por feature. Cada feature vive en `src/api/<feature>/` y expone `routes.py`, `service.py` y `repository.py`.

- **Flujo:** `routes → service → repository`.
- **Routes:** solo enlazan HTTP con el service.
- **Service:** orquesta el negocio (errores, imágenes, paginación).
- **Repository:** es la única capa que conoce SQLAlchemy y la única que hace commit.
- **Entidades:** prefijo de tabla `pf_*` y columnas `id_<tabla>`.
- **API:** los routers se montan bajo `/api`; los estáticos, bajo `/static`.
- **Auth:** `routes → service → google_service` (validación del token) y `session_repository` (refresh tokens). Es un módulo WIP sin montar. Contrato previsto: `POST /api/auth/google` recibe `googleToken` y devuelve `{ token, refresh_token, user }`, igual que espera `AuthService` del front.

## Decisiones técnicas

| Fecha | Estado | Decisión | Motivo | Alternativas descartadas |
|---|---|---|---|---|
| 2026-10-27 | Aceptado | Arquitectura por feature con `routes`, `service` y `repository`. | Aísla HTTP, negocio y persistencia; facilita tests y cambios. | Capas globales por tipo de archivo. |
| 2026-10-27 | Aceptado | El repository es la única capa que hace commit. | Evita commits parciales y dependencias cruzadas entre features. | Commits desde el service. |
| 2026-10-27 | Aceptado | Errores de dominio con RFC 9457 (`fastapi-problem` + `rfc9457`). | Respuestas uniformes y cliente predecible. | `HTTPException` sueltas. |
| 2026-10-27 | Aceptado | Los services lanzan `NotFoundError`; nunca devuelven `None` para "no encontrado". | El contrato de error queda explícito en una sola capa. | `None` como señal de ausencia. |
| 2026-10-27 | Aceptado | Las relaciones M:N de `project` se resuelven dentro del repository de `project` en un único commit. | Atomicidad y regla cross-feature: una feature no importa el repository de otra. | Features `project_language` / `project_technology`. |
| 2026-10-27 | Aceptado | Imágenes en Cloudinary; la BD guarda solo la URL. | Evita binarios en la base y simplifica el borrado idempotente. | Almacenamiento local o binarios en PostgreSQL. |
| 2026-10-27 | Aceptado | Prefijos `pf_*` en tablas e `id_<tabla>` en columnas; FKs con `Field(gt=0)`. | Evita colisiones y valida identificadores. | Nombres genéricos sin prefijo. |
| 2026-10-27 | Aceptado | Tests con `pytest`; los casos `@pytest.mark.live` se excluyen por defecto. | Los tests base no dependen de servicios externos reales. | Ejecutar `live` en cada corrida. |
| 2026-10-27 | Pendiente | Auth con Google OAuth + JWT: access token de 15 min y refresh token rotativo de 1 día en `pf_user_sessions`. | **No implementado.** Hay un módulo WIP (`src/api/auth/`) que no importa ni está montado. | Sesión en `sessionStorage` en el front (expuesta a XSS) o cookie `httpOnly` emitida por el BFF. |

## Estado

- API activa y refactorizada a la arquitectura por feature.
- `pytest`: 62 tests pasan.
- Auth **no implementado**: el módulo WIP no importa y el router no está montado. El resto de features funciona.
- [ ] Confirmar si el error 400 de `POST /api/project` sigue vigente y cuál es su causa.

## Pendientes

- **Auth (no implementado):** `src/api/auth/` es WIP y hoy no se puede importar: `EmailStr` necesita `email-validator`, falta la librería JWT, `src/core/security.py` y `src/api/users/service.py` no existen, los modelos `User`/`Role`/`UserSession` y las tablas `pf_users`, `pf_roles` y `pf_user_sessions` no están, y el router no está incluido en `main.py`. No tocar hasta decidir el alcance.
- **GitHub y Apple:** `config.py` y `.env_demo` declaran credenciales, pero no hay validación de esos proveedores; quedan fuera hasta que se implemente auth.
- **Error 400 en `POST /api/project`:** aparcado; no crítico por ahora.

## Problemas conocidos

- El error 400 de creación de `project`.
- El módulo de auth no se puede importar (ver Pendientes).

## Deuda técnica

- El login OAuth/JWT no está implementado y le faltan dependencias (librería JWT y `email-validator`).
- `google_service` fija las URLs de Google en constantes en vez de leer `GOOGLE_TOKEN_INFO_URL` y `GOOGLE_USERINFO_URL` del entorno.
- `live` depende de servicios externos reales; no se ejecuta en la suite por defecto.
