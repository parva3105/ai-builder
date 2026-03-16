# Current State

## Repository basics
- Repo initialized: yes (git present)
- Remote connected: no (not yet pushed)
- Default branch: main
- M0 (bootstrap): complete
- M1 (backend foundation): complete
- M2 (frontend foundation): complete
- CI configured: yes (`.github/workflows/ci.yml`)

## Current stack
- Frontend: Next.js 14 + TypeScript (App Router)
- Backend: FastAPI + Python 3.11
- Database: PostgreSQL 16 (via Docker Compose)
- Auth: JWT (access + refresh tokens) – bcrypt for password hashing
- API style: REST + OpenAPI 3.1
- File storage: local filesystem (dev), S3-compatible (prod – not yet built)
- LLM: OpenAI GPT-4o
- LaTeX: sandboxed pdflatex via Docker
- Testing: pytest (backend), Jest/Vitest (frontend), Playwright (e2e)
- Infra: Docker Compose (local), GitHub Actions (CI)

## Current top-level structure present
- `.agents/` – rules and skills
- `.specify/` – constitution
- `.github/workflows/` – CI pipeline
- `apps/api/` – FastAPI backend (models, auth, migrations configured)
- `apps/web/` – Next.js frontend (shell, auth pages, dashboard)
- `tests/backend/` – pytest (health + auth unit + auth integration)
- `tests/e2e/` – Playwright placeholder
- `docs/` – memory, runbooks, primer
- `PRODUCT.md`, `ARCHITECTURE.md`, `TASKS.md`, `README.md`
- `openapi.yaml` – v1 API contract (14 endpoints)
- `docker-compose.yml` – db, api, web, latex services
- `.env.example` – all required env vars
- `.gitignore`

## What exists right now
- Full project scaffold (backend + frontend + tests + infra)
- 4 ORM models: User, MasterResume, TailoringRequest, GeneratedOutput
- Alembic configured for async migrations (`alembic.ini`, `app/db/migrations/`)
- Auth endpoints: register, login, refresh, me (matching openapi.yaml)
- JWT auth dependency (`api/deps.py`) for protected routes
- Auth service with business logic separated from routes
- Pydantic schemas for all auth request/response types
- 29 passing tests (health smoke, auth service unit, auth endpoint integration)
- Test infrastructure: SQLite in-memory + ASGI TestClient (no PostgreSQL needed)
- Frontend: app shell, landing page, login/signup pages, protected dashboard, /resumes page with temporary mocks
- M3 Frontend UI components: ResumeCard, ResumeList, UploadResumeModal with typed temporary hooks.

## What does not exist yet
- Initial Alembic migration file (requires live PostgreSQL to run `alembic revision --autogenerate`)
- Tailoring engine / LLM integration (M4)
- Output generation / download endpoints (M5)
- Frontend dashboard features (M3+)
- Production file storage adapter (S3)
- End-to-end tests

## Current branch
- main

## Current priority
- M3: File management frontend (connect UI to backend)
- M4: Tailoring engine (LLM integration, request creation, status)
- Prerequisite: Alembic migration (live PostgreSQL)
- M4: Tailoring engine (LLM integration, request creation, status)

## Current blockers
- Initial Alembic migration needs live PostgreSQL (`docker compose up -d db`)
- OpenAI API key needed for M4
- Docker required for LaTeX compilation tests

## Last completed milestone
- M1: Backend foundation (models, Alembic, auth endpoints, tests)
- M2: Frontend foundation (app shell, auth pages, routing)
- M3: File management backend (upload, list, update, delete endpoints)