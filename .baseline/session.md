# Sesión

> Checkpoint local (fuera de Git): el punto de continuación de la tarea en curso, no un diario.
> Mantenlo corto (≤ ~40 líneas) y reemplaza su contenido en vez de acumular. Sin transcripciones ni secretos.

## Tarea activa

Poner la memoria al día. Auth queda **fuera de alcance**: no está implementado y no se toca.

## Último avance comprobado

`pytest`: 62 tests pasan con language, technology, project, url y url-grp. `src/api/auth/` existe como WIP (sin commit), no se puede importar y no está montado en `main.py`.

## Archivos tocados

- `DEVELOPMENT.md`
- `.baseline/session.md`

## Pruebas ejecutadas y resultado real

- `.venv\Scripts\python.exe -m pytest -q`: 62 passed.
- `python -c "import src.api.auth.routes"`: falla por `EmailStr` sin `email-validator`.
- `grep auth src/main.py`: sin resultados (router no montado).

## Bloqueos

- Ninguno en las features activas.
- Auth sin implementar: faltan `src/core/security.py`, `src/api/users/`, modelos y tablas de usuario, librería JWT y el montaje del router.

## Siguiente paso

Ninguno autorizado sobre auth. Si se retoma, primero decidir alcance (solo Google o también GitHub/Apple, librería JWT y rol inicial).
