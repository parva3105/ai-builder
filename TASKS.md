# Tasks

This file is the primary milestone and execution tracker for both humans and AI agents.

## Working rules
- Keep tasks concrete and implementation-friendly.
- Prefer vertical slices where possible.
- Update this file whenever major work is completed, blocked, or reprioritized.
- Keep this aligned with the memory layer.

---

## M0 – Foundations and Planning ✅
- [x] Finalize product framing in `PRODUCT.md`
- [x] Expand `ARCHITECTURE.md` with domain model, auth, file storage, LaTeX strategy
- [x] Confirm stack: Next.js + FastAPI + PostgreSQL + JWT + Docker
- [x] Scaffold `apps/api/` (FastAPI backend structure)
- [x] Scaffold `apps/web/` (Next.js frontend structure)
- [x] Scaffold `tests/` (backend + e2e placeholders)
- [x] Create `.env.example`
- [x] Create `docker-compose.yml` with db, api, web, latex services
- [x] Create `.github/workflows/ci.yml`
- [x] Create `docs/runbooks/local-setup.md`
- [x] Expand `openapi.yaml` with v1 endpoints
- [x] Update memory files after bootstrap

### Exit criteria
- Project structure exists ✅
- Docs are readable ✅
- Repo is ready for backend and frontend parallel work ✅

---

## M1 – Backend Foundation ✅
- [x] Install dependencies and verify app boots (`uvicorn app.main:app`)
- [x] Configure Alembic for database migrations
- [x] Create User model (SQLAlchemy ORM)
- [x] Create MasterResume model
- [x] Create TailoringRequest model
- [x] Create GeneratedOutput model
- [ ] Run initial migration to create tables *(requires live PostgreSQL)*
- [x] Implement `POST /auth/register` endpoint
- [x] Implement `POST /auth/login` endpoint
- [x] Implement `POST /auth/refresh` endpoint
- [x] Implement `GET /auth/me` endpoint
- [x] Add auth dependency (extract user from JWT)
- [x] Write unit tests for auth service
- [x] Write integration tests for auth endpoints
- [x] Verify health endpoint works end-to-end

### Exit criteria
- Backend boots locally ✅
- Health check responds ✅
- Auth register/login/refresh/me work ✅
- Database tables exist via migration *(pending live DB)*
- Tests pass ✅ (29 passing)

---

## M2 – Frontend Foundation ✅
- [x] Create app layout with navigation shell
- [x] Create global CSS baseline (no Tailwind)
- [x] Create login page
- [x] Create signup page
- [x] Create dashboard page (placeholder)
- [x] Implement auth context/state management
- [x] Connect login/signup to backend API
- [x] Create protected route wrapper
- [x] Handle loading/error/empty states
- [x] Add basic responsive design

### Exit criteria
- Frontend boots locally ✅
- User can navigate login → signup → dashboard ✅
- Auth flow connects to backend or uses mock data ✅
- UX states are handled ✅

---

## M3 – File Management
- [ ] Implement `POST /resumes/upload` (backend)
- [ ] Implement `GET /resumes` (backend)
- [ ] Implement `GET /resumes/{id}` (backend)
- [ ] Implement `PATCH /resumes/{id}` (backend – rename)
- [ ] Implement `DELETE /resumes/{id}` (backend)
- [ ] Create file storage service (local filesystem)
- [ ] Validate file types and sizes server-side
- [ ] Create resume upload UI component (frontend)
- [ ] Create resume list/management page (frontend)
- [ ] Connect frontend to resume API endpoints
- [ ] Write tests for upload/list/delete flows

### Exit criteria
- User can upload .tex and .docx files
- User can list, rename, and delete uploaded resumes
- Files are stored per-user in isolated directories
- File validation enforced

---

## M4 – Tailoring Engine
- [ ] Create OpenAI service layer (backend)
- [ ] Design prompt templates for each action type
- [ ] Implement `POST /tailoring/requests` (backend)
- [ ] Implement `GET /tailoring/requests/{id}` (backend)
- [ ] Handle tailor_tex action (LLM → .tex → PDF via sandbox)
- [ ] Handle tailor_docx action (LLM → .docx via python-docx)
- [ ] Handle cover_letter action (LLM → .docx or .txt)
- [ ] Create job description input UI (frontend)
- [ ] Create action selection UI (frontend)
- [ ] Create processing status UI (frontend)
- [ ] Connect frontend to tailoring API endpoints
- [ ] Write tests for tailoring service

### Exit criteria
- User can paste a job description and choose an action
- System processes the request and generates output
- Status is visible during processing
- Errors are surfaced clearly

---

## M5 – Download & Output
- [ ] Implement `GET /outputs/{id}` (backend)
- [ ] Implement `GET /outputs/{id}/download` (backend)
- [ ] Configure LaTeX sandbox compilation
- [ ] Generate filenames like `FirstName_LastName_Resume_CompanyName.pdf`
- [ ] Create output review UI (frontend)
- [ ] Create download button/flow (frontend)
- [ ] Show per-user output history (frontend)
- [ ] Write tests for output retrieval and download

### Exit criteria
- User can review and download generated outputs
- PDF compilation works for valid .tex
- Compilation errors are reported clearly
- Output history is visible

---

## M6 – Validation & Stabilization
- [ ] Tighten lint checks (ruff for backend, ESLint for frontend)
- [ ] Tighten type checks (mypy for backend, tsc for frontend)
- [ ] Fix any failing tests
- [ ] Add integration tests for core workflows
- [ ] Add e2e tests (Playwright) for critical user journeys
- [ ] Improve error messages and logging
- [ ] Improve developer documentation
- [ ] Review security-sensitive areas
- [ ] Resolve known blockers

### Exit criteria
- Repo is stable
- Validation is reproducible
- No critical blockers remain

---

## M7 – Release Readiness
- [ ] Confirm local setup steps work end-to-end
- [ ] Confirm Docker Compose builds and runs
- [ ] Confirm all env vars documented
- [ ] Confirm deployment assumptions
- [ ] Run smoke test
- [ ] Create release checklist
- [ ] Finalize backlog for v2

### Exit criteria
- A reviewer can clone, run, and validate the project
- Release steps are documented

---

## Current Priority
- **M3: File management** (resume upload, list, get, update, delete)
- Prerequisite: run initial Alembic migration with live PostgreSQL
- M1 and M2 are complete.

## Known Blockers
- OpenAI API key needed for M4 (tailoring engine)
- Docker required for LaTeX compilation (M5)
- S3 adapter needed for production file storage (post-v1)

## Backlog
- [ ] S3/R2 storage adapter for production
- [ ] Rate limiting on API endpoints
- [ ] Webhook/callback for long-running tailoring jobs
- [ ] Side-by-side diff view (original vs. tailored resume)
- [ ] Multiple tailoring style modes (ATS, concise, achievement-heavy)
- [ ] Output retention policy
- [ ] ADR process if architecture grows
- [ ] Observability dashboards
- [ ] Background job queue (Celery/Redis) if tailoring is too slow inline