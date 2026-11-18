# Sesión

> Checkpoint local (fuera de Git): el punto de continuación de la tarea en curso, no un diario.
> Mantenlo corto (≤ ~40 líneas) y reemplaza su contenido en vez de acumular. Sin transcripciones ni secretos.

## Tarea activa

Restricción de acceso a los endpoints del backend: todos los recursos (`project`, `language`, `technology`, `url`, `url-grp`) siguen el patrón de solo `GET /` público y el resto (pagination, by-id, escritura) exige `require_admin`. Completado.

## Último avance comprobado

Los cinco recursos (`project`, `language`, `technology`, `url`, `url-grp`) tienen `require_admin` en pagination, by-id y escritura. `GET /` queda público (solo `verify_api_key`). `url-grp` además mantiene `GET /detail` público (footer del HOME). Sin promoción automática: el rol `admin` se asigna manualmente en la BD. Import de `src.main` OK. Verificado por HTTP vía BFF: `GET /project/` → 200, `GET /project/pagination` → 401, `GET /project/20` → 401, `POST /project/` → 401 (sin sesión).

## Archivos tocados

- `src/api/project/routes.py`, `src/api/language/routes.py`, `src/api/technology/routes.py`, `src/api/url/routes.py`, `src/api/url_grp/routes.py`
- `src/api/auth/service.py`
- `src/core/config.py`
- `.env.example`
- `DEVELOPMENT.md`
- `.baseline/session.md`

## Pruebas ejecutadas y resultado real

- `python -c "import src.main"`: OK.
- HTTP vía BFF: GET project → 200; pagination → 401; by-id → 401; POST → 401.
- `pytest` no ejecutado (drop_all).

## Bloqueos

- Los tests de escritura necesitan override de `require_admin` en el fixture (pendiente).

## Siguiente paso

Actualizar los tests de `project`, `language`, `technology`, `url` y `url-grp` para overridear `require_admin` en los casos de escritura.
