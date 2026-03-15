# Architecture

## Status
This file is the living architecture document for the project.
It starts as a structured placeholder and should be expanded and refined by the architect-planner skill as the project evolves.

## Current recommended baseline
If the product does not explicitly require a different stack, the default baseline is:

- Frontend: Next.js + TypeScript
- Backend: FastAPI + Python
- Database: PostgreSQL
- Background jobs: optional worker process if needed
- Infra: Docker Compose locally, GitHub Actions for CI
- API contract: OpenAPI-based REST
- Testing: unit, integration, and e2e

## Architecture goals
- Keep the initial architecture simple and modular.
- Enable parallel development between backend, frontend, QA, and bugfix agents.
- Make the repository easy to scaffold and extend.
- Favor explicit contracts and predictable boundaries.
- Avoid premature microservices unless the product clearly needs them.

## Proposed top-level structure
- `apps/web/` for the frontend application
- `apps/api/` for the backend API
- `packages/` for reusable shared modules if needed
- `tests/` for integration, e2e, fixtures, and smoke validation
- `docs/` for reference material, runbooks, and memory
- `.agents/` for rules and skills guiding agent behavior

## Expected system boundaries
### Frontend
Responsible for:
- screens and routes
- reusable UI components
- state and client-side data flow
- API integration
- UX states such as loading, error, empty, success

### Backend
Responsible for:
- request routing
- auth/session handling
- business logic
- persistence layer
- input/output validation
- API contract consistency
- backend logs and operational safety

### Shared contracts
Responsible for:
- API definitions
- shared types or schemas where appropriate
- stable request/response expectations

### QA/Validation
Responsible for:
- linting
- type checking
- unit/integration/e2e strategy
- CI quality gates
- stability reporting
- reproducible validation steps

## Expected module layering
### Backend layering
- `api/` for routes, request entry points, and dependencies
- `schemas/` for request/response models
- `services/` for business logic
- `models/` for ORM or domain models
- `db/` for session and migration handling
- `core/` for configuration, auth helpers, logging, and shared internal utilities

### Frontend layering
- `app/` or routing layer for pages/routes
- `components/` for reusable UI
- `features/` for domain-specific modules
- `hooks/` for reusable behavior
- `lib/` for API clients and infrastructure helpers
- `types/` for frontend-safe types

## Data model guidance
The architect agent should refine the entities below based on the actual product.

Minimum categories to define:
- User
- Session or auth state if applicable
- Core domain entities for the product
- Audit or operational metadata where needed

For each important entity, define:
- name
- fields
- ownership
- relationships
- lifecycle
- validation constraints

## API guidance
- Prefer clear REST endpoints to start.
- Document request and response schemas.
- Keep error responses explicit and structured.
- Versioning is optional at first, but route structure should allow future evolution.
- Update `openapi.yaml` whenever endpoint behavior changes.

## Auth guidance
- Use secure defaults.
- Keep secrets in environment variables.
- Decide early whether auth is required for v1.
- If auth is present, document:
  - session/token flow
  - protected resources
  - user identity boundaries
  - permission model

## Observability guidance
Even for early versions:
- log important failures
- log startup success/failure
- log request-level errors safely
- avoid leaking secrets in logs

## Performance guidance
- Avoid premature optimization.
- Prioritize clarity and correctness first.
- Identify only obviously hot paths.
- Make the architecture compatible with later caching, async jobs, or queue-based work if the product needs it.

## Security guidance
- never hardcode secrets
- validate inputs
- restrict privileged operations
- keep configuration explicit
- document security-sensitive decisions

## Deployment guidance
Initial deployment should be straightforward:
- containerized apps
- environment-based configuration
- CI checks before merge
- documented local setup
- simple release path

## Architecture decisions log
Major decisions should also be reflected in:
- `docs/memory/decisions.md`
- `docs/memory/current-state.md`
- ADR-style notes if the project grows

## Known gaps
- Final domain model not yet defined
- Final endpoint list not yet defined
- Final auth strategy not yet chosen
- Final deployment target not yet chosen