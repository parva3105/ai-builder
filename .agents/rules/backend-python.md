---
trigger: glob
globs: apps/api/**/*.py
---

# Backend Python Rule

Apply this rule to backend Python files.

## Backend structure guidance
- Keep routes thin.
- Keep business logic in services.
- Keep schemas and models explicit.
- Keep configuration centralized.
- Prefer typed functions and clear return shapes.
- Make boundary validation obvious.

## Suggested layout
- `api/routes/` for route handlers
- `api/deps/` for dependencies
- `api/schemas/` for request/response models if colocated
- `services/` for business logic
- `models/` for persistence/domain models
- `db/` for session, connection, and migration concerns
- `core/` for config, auth helpers, logging, and common backend helpers

## FastAPI-style guidance
- Prefer explicit request/response models
- Validate inputs at the route boundary
- Keep dependency injection understandable
- Avoid putting large business logic blocks directly in route functions

## Error handling guidance
- raise or map errors consistently
- avoid swallowing exceptions without context
- do not leak sensitive internal details

## Testing guidance
- business logic should be testable without the full app
- route behavior should be covered through integration tests where relevant
- use fixtures cleanly