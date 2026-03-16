# Iteration Log

This file is chronological.
Append new entries at the top or bottom consistently.
Use concise, resume-friendly summaries.

---

## Iteration 004
- Date: 2026-03-16
- Agent/Role: frontend-builder
- Branch: main
- Objective: Fix React hydration state error and change frontend port to 3001.
- Summary of work: Changed frontend development and Docker port configuration from `3000` to `3001` globally (`package.json`, `config.py`, `docker-compose.yml`, docs). Fixed a Next.js 15+ React hydration error ("Can't perform a React state update on a component that hasn't mounted yet") inside `AuthContext.tsx` by moving the resolution of the initialization promise into a `useEffect`.
- Files changed:
  - `apps/web/src/contexts/AuthContext.tsx`
  - `apps/web/package.json`
  - `docker-compose.yml`
  - `apps/api/app/core/config.py`
  - `apps/web/Dockerfile`
  - `docs/runbooks/local-setup.md`
  - `apps/web/README.md`
- Tests/checks run:
  - `npm run lint` – ✅ no errors
  - `npm run build` – ✅ compiled cleanly
- Result: Frontend now runs reliably on port 3001 without hydration errors.
- Risks/notes: Hydration state is now slightly delayed until client-side mount (normal SPA behavior).
- Next recommended action: Run Alembic migration, then start M3 backend tasks.

---

## Iteration 003
- Date: 2026-03-16
- Agent/Role: memory-keeper
- Branch: main
- Objective: Update memory layer after M1 and M2 completion
- Summary of work: Updated TASKS.md to mark M1 as complete (checkboxes + exit criteria). Updated current priority from M1/M2 to M3. Rewrote next-actions.md to make M3 (file management) the immediate next milestone with Alembic migration as prerequisite. Verified current-state.md, decisions.md, and open-questions.md are accurate. No new durable decisions or open questions introduced.
- Files changed:
  - `TASKS.md` (marked M1 complete, updated current priority to M3)
  - `docs/memory/next-actions.md` (rewritten for M3 focus)
  - `docs/memory/iteration-log.md` (this entry)
- Tests/checks run: none (docs-only change)
- Result: Memory layer is current. All files reflect post-M1/M2 truth.
- Risks/notes: Initial Alembic migration still pending (requires live PostgreSQL).
- Next recommended action: Run Alembic migration, then start M3 backend tasks.

---

## Iteration 002
- Date: 2026-03-16
- Agent/Role: backend-builder
- Branch: main
- Objective: M1 – Backend Foundation
- Summary of work: Implemented the complete backend foundation for TailorFlow. Created 4 ORM models (User, MasterResume, TailoringRequest, GeneratedOutput) with enums and relationships matching ARCHITECTURE.md. Configured Alembic for async migrations. Built auth layer: Pydantic schemas (6 classes matching openapi.yaml), auth service (register, login, refresh, user lookup), JWT auth dependency (HTTPBearer + token decode + user resolve), and auth router (4 thin endpoints). Replaced passlib with direct bcrypt due to incompatibility with bcrypt 5.x. Set up test infrastructure with SQLite in-memory + ASGI TestClient. All 29 tests pass.
- Files created:
  - `apps/api/app/models/user.py`
  - `apps/api/app/models/master_resume.py`
  - `apps/api/app/models/tailoring_request.py`
  - `apps/api/app/models/generated_output.py`
  - `apps/api/app/schemas/auth.py`
  - `apps/api/app/services/auth_service.py`
  - `apps/api/app/api/deps.py`
  - `apps/api/app/api/auth.py`
  - `apps/api/alembic.ini`
  - `apps/api/app/db/migrations/env.py`
  - `apps/api/app/db/migrations/script.py.mako`
  - `apps/api/app/db/migrations/versions/.gitkeep`
  - `tests/backend/test_auth_service.py`
  - `tests/backend/test_auth_endpoints.py`
- Files changed:
  - `apps/api/app/main.py` (added auth router)
  - `apps/api/app/core/security.py` (replaced passlib with direct bcrypt)
  - `apps/api/app/models/__init__.py` (re-exports all models)
  - `apps/api/app/schemas/__init__.py` (re-exports auth schemas)
  - `apps/api/app/services/__init__.py` (re-exports auth_service)
  - `apps/api/pyproject.toml` (fixed hatch build, swapped passlib→bcrypt, added aiosqlite)
  - `tests/backend/conftest.py` (SQLite test DB, ASGI client, fixtures)
  - `tests/backend/test_health.py` (switched to ASGI TestClient)
- Tests/checks run:
  - `python -c "from app.main import app"` – ✅ boot OK
  - `python -m pytest ../../tests/backend/ -v` – ✅ 29 passed in 5.5s
- Result: M1 complete. Backend boots, all auth endpoints work, all tests pass.
- Risks/notes: Initial Alembic migration not generated yet (requires live PostgreSQL).
- Next recommended action: Run initial Alembic migration with live DB, then start M3 (file management).

---

## Iteration 001
- Date: 2026-03-15
- Agent/Role: frontend-builder
- Branch: main
- Objective: M2 – Frontend Foundation
- Summary of work: Implemented the complete frontend foundation for TailorFlow. Created a premium dark-first design system with vanilla CSS (glassmorphism, gradient accents, micro-animations). Built auth context with JWT token persistence and automatic hydration. Created responsive navigation shell with mobile hamburger menu. Built 5 reusable UI components (Button, Input, LoadingSpinner, ErrorMessage, EmptyState). Implemented landing page with animated gradient orbs, login/signup pages with form validation and error handling, and a protected dashboard page with placeholder feature cards.
- Files created:
  - `apps/web/src/types/api.ts`
  - `apps/web/src/contexts/AuthContext.tsx`
  - `apps/web/src/components/ProtectedRoute.tsx`
  - `apps/web/src/components/Navbar.tsx`
  - `apps/web/src/components/Navbar.module.css`
  - `apps/web/src/components/ui/Button.tsx`
  - `apps/web/src/components/ui/Input.tsx`
  - `apps/web/src/components/ui/LoadingSpinner.tsx`
  - `apps/web/src/components/ui/ErrorMessage.tsx`
  - `apps/web/src/components/ui/EmptyState.tsx`
  - `apps/web/src/components/ui/ui.module.css`
  - `apps/web/src/app/providers.tsx`
  - `apps/web/src/app/home.module.css`
  - `apps/web/src/app/login/page.tsx`
  - `apps/web/src/app/login/page.module.css`
  - `apps/web/src/app/signup/page.tsx`
  - `apps/web/src/app/signup/page.module.css`
  - `apps/web/src/app/dashboard/page.tsx`
  - `apps/web/src/app/dashboard/page.module.css`
- Files changed:
  - `apps/web/src/app/globals.css` (replaced with design system)
  - `apps/web/src/app/layout.tsx` (Inter font, TailorFlow metadata, AuthProvider)
  - `apps/web/src/app/page.tsx` (replaced with landing page)
- Files deleted:
  - `apps/web/src/app/page.module.css` (replaced by `home.module.css`)
- Tests/checks run:
  - `npm run build` – ✅ compiled in 5.6s, all 5 routes generated
  - `npm run lint` – ✅ no errors
- Result: M2 complete. Frontend boots, all routes render, auth flow connects to API.
- Risks/notes: Auth flow requires M1 backend endpoints to work end-to-end. Currently handles API errors gracefully with user-visible messages.
- Next recommended action: Complete M1 (backend foundation) to enable end-to-end auth testing.

---

## Writing guidance
- Keep entries factual
- Mention commands/checks if relevant
- Make the next step obvious
- Do not duplicate long diffs here