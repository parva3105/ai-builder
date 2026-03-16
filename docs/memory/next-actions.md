# Next Actions

## Prerequisite – Initial Alembic migration
1. Create `.env` from `.env.example` with real DB credentials
2. Start PostgreSQL: `docker compose up -d db`
3. Generate migration: `cd apps/api && alembic revision --autogenerate -m "initial_tables"`
4. Apply migration: `alembic upgrade head`
5. Verify all 4 tables exist (users, master_resumes, tailoring_requests, generated_outputs)

### Recommended owner
- backend-builder skill

### Definition of done
- Migration file committed under `apps/api/app/db/migrations/versions/`
- Tables exist in PostgreSQL

---

## Immediate next milestone – M3: File Management

### Backend tasks
1. Create file storage service (`apps/api/app/services/file_service.py`) – local filesystem adapter
2. Create resume Pydantic schemas (`apps/api/app/schemas/resume.py`)
3. Implement `POST /resumes/upload` – multipart upload, validate type/size, store file, create DB row
4. Implement `GET /resumes` – list user's resumes
5. Implement `GET /resumes/{resume_id}` – get single resume metadata
6. Implement `PATCH /resumes/{resume_id}` – rename resume
7. Implement `DELETE /resumes/{resume_id}` – delete resume and file
8. Write integration tests for all resume endpoints

### Frontend tasks
- [x] Create resume upload component
- [x] Create resume list/management page
- [x] Connect frontend to resume API endpoints (implemented using `useResumes` hook with typed mocks)

### Recommended owner
- Backend: backend-builder skill
- Frontend: frontend-builder skill

### Notes for the next agent
- Auth infrastructure is in place – use `get_current_user` dependency for protected routes
- Test infrastructure is ready – use `client` and `db_session` fixtures from `tests/backend/conftest.py`
- File paths should include `user_id` for per-user isolation (see `ARCHITECTURE.md`)
- openapi.yaml defines the contract for resume endpoints
- Frontend M3 is currently mocked via `src/hooks/useResumes.ts`. When the backend is ready, the API client `src/lib/api.ts` will naturally route to the backend. Just ensure the backend exactly adheres to `openapi.yaml`.
- Backend for M3 is built conceptually, but Docker must be started so the user can run `alembic init` migrations before the frontend can successfully use it in e2e flows.
- Do not start M4 until M3 frontend is un-mocked and working end-to-end.

### Definition of done
- User can upload .tex and .docx files via API
- User can list, rename, and delete uploaded resumes
- Files stored per-user in isolated directories
- File type/size validation enforced
- Integration tests pass