# Decisions

This file records durable decisions that should survive across many iterations.

---

### [2026-03-15] Stack selection confirmed
- Status: accepted
- Context:
  - PRODUCT.md defined a default stack; bootstrap run needed to confirm
- Decision:
  - Frontend: Next.js 14 + TypeScript (App Router)
  - Backend: FastAPI + Python 3.11
  - Database: PostgreSQL 16
  - Auth: JWT (HS256, access + refresh tokens)
  - File storage: local filesystem (dev), S3-compatible (prod)
  - LLM: OpenAI GPT-4o
  - LaTeX: sandboxed pdflatex via Docker container
  - Infra: Docker Compose (local), GitHub Actions (CI)
  - API: REST + OpenAPI 3.1
- Rationale:
  - Matches PRODUCT.md defaults; well-supported, simple, production-ready
- Consequences:
  - All scaffold files follow this stack
  - Future agents should not switch stack without explicit approval
- Follow-up:
  - None

### [2026-03-15] Domain model defined
- Status: accepted
- Context:
  - Needed to define entities before backend implementation
- Decision:
  - 4 core entities: User, MasterResume, TailoringRequest, GeneratedOutput
  - User owns all other entities; queries scoped by user_id
  - File storage paths include user_id for isolation
- Rationale:
  - Minimum viable model covering auth, file management, tailoring, and output
- Consequences:
  - Backend models, schemas, and endpoints follow this structure
  - openapi.yaml reflects these entities
- Follow-up:
  - Create ORM models in M1

### [2026-03-15] Auth strategy: JWT access + refresh tokens
- Status: accepted
- Context:
  - Needed auth approach before implementing endpoints
- Decision:
  - Access tokens: 30-min expiry, HS256
  - Refresh tokens: 7-day expiry
  - Secrets from env vars, never hardcoded
  - bcrypt for password hashing
- Rationale:
  - Simple, stateless, fits REST API; no session store needed
- Consequences:
  - No server-side session invalidation (acceptable for v1)
  - Refresh token rotation not implemented yet
- Follow-up:
  - Implement auth endpoints in M1

### [2026-03-15] LaTeX compilation: sandboxed Docker container
- Status: accepted
- Context:
  - .tex files can contain dangerous commands; needed safe compilation strategy
- Decision:
  - Use a dedicated TeXLive Docker container
  - No shell-escape flag
  - Configurable timeout (default 60s)
  - Shared volume for file exchange
- Rationale:
  - Complete isolation from API server; safe by default
- Consequences:
  - Docker required for LaTeX features
  - Slight latency for compilation (acceptable)
- Follow-up:
  - Configure sandbox in M5

### [2026-03-15] Monorepo structure: apps/api + apps/web
- Status: accepted
- Context:
  - Needed to decide between monorepo or separate repos
- Decision:
  - Single repo with `apps/api/` and `apps/web/` directories
  - Shared `tests/`, `docs/`, and infrastructure at root
- Rationale:
  - Simpler for a small team / agent workflow; everything in one place
- Consequences:
  - CI runs both backend and frontend checks
  - Docker Compose manages all services from root
- Follow-up:
  - None

### [2026-03-16] Replaced passlib with direct bcrypt
- Status: accepted
- Context:
  - passlib 1.7.x is incompatible with bcrypt 5.x (removed `__about__` attribute, changed password length validation)
  - Password hashing was broken in tests and at runtime
- Decision:
  - Removed `passlib[bcrypt]` from dependencies
  - Added `bcrypt>=4.1,<6` as direct dependency
  - Rewrote `app/core/security.py` to use `bcrypt.hashpw()` and `bcrypt.checkpw()` directly
- Rationale:
  - passlib is unmaintained; direct bcrypt is simpler and more reliable
- Consequences:
  - No passlib CryptContext available; hashing is done via raw bcrypt calls
  - If passlib is needed later for other hash schemes, it would need a compatible version
- Follow-up:
  - None

---

## Decision template
Use the format above when adding a decision.