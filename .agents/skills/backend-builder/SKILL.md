---
name: backend-builder
description: Build or extend the backend foundation and features, including scaffolding, routes, schemas, services, models, persistence integration, validation, and backend tests.
---

# Purpose
Use this skill for backend implementation work.

# Read first
- `PRODUCT.md`
- `ARCHITECTURE.md`
- `TASKS.md`
- `docs/primer.md`
- `docs/memory/current-state.md`
- `docs/memory/next-actions.md`
- `openapi.yaml` when relevant
- `.agents/rules/project-context.md`
- `.agents/rules/backend-python.md`
- `.agents/rules/testing-and-quality.md`
- `.agents/rules/security-and-secrets.md`

# Default scope
- `apps/api/**`
- backend-related shared code
- `tests/integration/**`
- backend runtime/config files if needed

# Primary responsibilities
- scaffold backend structure if missing
- implement app startup and configuration
- implement routes
- implement request/response schemas
- implement service-layer logic
- implement models and persistence integration
- add validation and error handling
- add or update integration tests
- keep contracts aligned

# Constraints
- do not modify frontend implementation unless shared contracts demand it
- do not silently change API behavior without updating `openapi.yaml`
- avoid embedding business logic directly in routes
- keep modules cohesive and testable

# Output summary
Report:
- features/endpoints created or changed
- files created or changed
- validation/tests run
- risks or missing pieces
- next recommended backend or QA task