# Sesión

> Checkpoint local (fuera de Git): el punto de continuación de la tarea en curso, no un diario.
> Mantenlo corto (≤ ~40 líneas) y reemplaza su contenido en vez de acumular. Sin transcripciones ni secretos.

## Tarea activa

El contrato de auth está alineado con el frontend (cookies HttpOnly en el BFF). Pendientes reales del backend: tests de auth, proveedores GitHub/Apple y el error 400 en `POST /api/project`.

## Último avance comprobado

`src/main.py` importa e incluye `auth_router` bajo `/api`: existen `/api/auth/{google,login,register,refresh,logout,me}`. `src/core/security.py` resuelve JWT, `verify_api_key`, `require_user` y `require_admin`; las tablas de auth están en `postgre_auth.sql` y los modelos en `src/models/auth_models.py`. El BFF consume `access_token` y el flujo está verificado por HTTP. La fila stale de "contrato desalineado" se eliminó de la memoria.

## Archivos tocados

- `DEVELOPMENT.md`
- `.baseline/session.md`

## Pruebas ejecutadas y resultado real

- 62 funciones `test_` en `tests/` (language 12, project 13, technology 12, url 12, url_grp 13); la última corrida registrada da 62 pasan.
- `pytest` **no** se ejecutó: el fixture `setup_db` hace `create_all`/`drop_all` sobre `TEST_DATABASE_URL` o `DATABASE_URL`, que puede ser la BD en uso.
- Comprobación HTTP contra la API local: 401 sin `X-API-Key` en rutas de auth y de portfolio.

## Bloqueos

- Auth sin cobertura de tests.
- GitHub y Apple sin validación.

## Siguiente paso

Aislar el fixture de tests (transacción o BD dedicada) y agregar casos para `google`, `refresh`, `logout` y `X-API-Key`.
