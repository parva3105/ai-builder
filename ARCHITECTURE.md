# Architecture

## Status
Expanded during M0 bootstrap (2026-03-15). This is the living architecture document for TailorFlow.

---

## Confirmed Stack

| Layer | Choice | Notes |
|-------|--------|-------|
| Frontend | Next.js 14 + TypeScript | App Router, `src/` directory layout |
| Backend | FastAPI + Python 3.11 | Async, Pydantic v2 |
| Database | PostgreSQL 16 | Async via SQLAlchemy + asyncpg |
| Auth | JWT (access + refresh tokens) | python-jose, bcrypt via passlib |
| File storage | Local filesystem (dev), S3-compatible (prod) | Uploads dir, per-user isolation |
| LLM | OpenAI GPT-4o | Resume tailoring + cover letter generation |
| LaTeX compilation | Sandboxed `pdflatex` via Docker | No shell escape, timeout, resource limits |
| DOCX processing | python-docx | Direct .docx manipulation |
| Infra | Docker Compose (local), GitHub Actions (CI) | Multi-stage Dockerfiles |
| API style | REST + OpenAPI 3.1 | Contract-first, `openapi.yaml` |
| Testing | pytest (backend), Jest/Vitest (frontend), Playwright (e2e) | CI integrated |

---

## Top-Level Structure

```
Project3/
├── apps/
│   ├── api/              # FastAPI backend
│   │   ├── app/
│   │   │   ├── api/      # Route handlers
│   │   │   ├── core/     # Config, security, logging
│   │   │   ├── db/       # Session, base, migrations
│   │   │   ├── models/   # SQLAlchemy ORM models
│   │   │   ├── schemas/  # Pydantic request/response
│   │   │   ├── services/ # Business logic
│   │   │   └── main.py   # FastAPI entry point
│   │   ├── Dockerfile
│   │   └── pyproject.toml
│   └── web/              # Next.js frontend
│       ├── src/
│       │   ├── app/      # App Router pages
│       │   ├── lib/      # API client, utilities
│       │   └── ...
│       ├── Dockerfile
│       └── package.json
├── tests/
│   ├── backend/          # pytest tests
│   └── e2e/              # Playwright tests
├── docs/
│   ├── memory/           # Agent memory layer
│   └── runbooks/         # Operational guides
├── .github/workflows/    # CI pipeline
├── docker-compose.yml
├── .env.example
├── openapi.yaml
├── PRODUCT.md
├── ARCHITECTURE.md
├── TASKS.md
└── README.md
```

---

## System Boundaries

### Frontend (apps/web)
- Screens and routes (App Router)
- Reusable UI components
- Client-side state and data flow
- API integration via typed fetch wrapper (`src/lib/api.ts`)
- UX states: loading, error, empty, success

### Backend (apps/api)
- Request routing (FastAPI routers)
- Auth/session handling (JWT)
- Business logic (services layer)
- Persistence (SQLAlchemy async)
- Input/output validation (Pydantic schemas)
- File processing (upload, parse, generate)
- API contract consistency with `openapi.yaml`

### LaTeX Sandbox
- Isolated Docker container with TeXLive
- Invoked on-demand by the API via `docker compose run --rm`
- No shell escape, controlled packages, timeouts
- Input: `.tex` file path; Output: compiled `.pdf` or error

---

## Domain Model

### User
| Field | Type | Notes |
|-------|------|-------|
| id | UUID | Primary key |
| email | string | Unique, validated |
| password_hash | string | bcrypt |
| full_name | string | Display name |
| created_at | timestamp | Auto |
| updated_at | timestamp | Auto |

### MasterResume
| Field | Type | Notes |
|-------|------|-------|
| id | UUID | Primary key |
| user_id | UUID | FK → User, ownership isolation |
| filename | string | Original upload name |
| format | enum | `tex` or `docx` |
| storage_path | string | File system path |
| display_name | string | User-editable label |
| created_at | timestamp | Auto |

### TailoringRequest
| Field | Type | Notes |
|-------|------|-------|
| id | UUID | Primary key |
| user_id | UUID | FK → User |
| resume_id | UUID | FK → MasterResume |
| job_description | text | Pasted by user |
| action | enum | `tailor_tex`, `tailor_docx`, `cover_letter` |
| status | enum | `pending`, `processing`, `completed`, `failed` |
| error_message | string | nullable, set on failure |
| created_at | timestamp | Auto |
| completed_at | timestamp | nullable |

### GeneratedOutput
| Field | Type | Notes |
|-------|------|-------|
| id | UUID | Primary key |
| request_id | UUID | FK → TailoringRequest |
| user_id | UUID | FK → User, redundant for quick access |
| filename | string | e.g. `John_Doe_Resume_Google.pdf` |
| format | enum | `pdf`, `docx`, `txt` |
| storage_path | string | File system path |
| created_at | timestamp | Auto |

### Entity Relationships
```
User 1──* MasterResume
User 1──* TailoringRequest
MasterResume 1──* TailoringRequest
TailoringRequest 1──0..1 GeneratedOutput
User 1──* GeneratedOutput
```

---

## Auth Strategy

### Flow
1. **Register**: `POST /auth/register` → creates user, returns access + refresh tokens
2. **Login**: `POST /auth/login` → validates credentials, returns tokens
3. **Refresh**: `POST /auth/refresh` → validates refresh token, returns new access token
4. **Protected routes**: require `Authorization: Bearer <access_token>` header

### Token Details
- Access token: 30-minute expiry, contains `sub` (user ID), `type: access`
- Refresh token: 7-day expiry, contains `sub` (user ID), `type: refresh`
- Algorithm: HS256
- Secret: loaded from `JWT_SECRET_KEY` env var

### User Isolation
- All data queries are scoped by `user_id` from the JWT
- No cross-user access to resumes, requests, or outputs
- File storage paths include user ID for filesystem isolation

---

## File Storage Strategy

### Development
- Local filesystem under `./uploads/`
- Directory structure: `uploads/{user_id}/resumes/` and `uploads/{user_id}/outputs/`

### Production
- S3-compatible object storage (e.g., AWS S3, MinIO, Cloudflare R2)
- Same logical path structure
- Storage layer abstracted behind a service interface for easy swap

### Upload Constraints
- Max file size: 10 MB (configurable via `MAX_UPLOAD_SIZE_MB`)
- Allowed formats: `.tex`, `.docx`
- File type validated server-side (not just extension)

---

## LaTeX Compilation Strategy

### Sandbox Approach
- Uses a dedicated TeXLive Docker container (no packages installed on the API server)
- API writes the `.tex` file to a shared volume, invokes compilation, reads the result

### Safety Controls
- **No shell escape**: `pdflatex` invoked without `-shell-escape`
- **Timeout**: configurable via `LATEX_COMPILE_TIMEOUT_SECONDS` (default 60s)
- **Resource limits**: Docker container runs with CPU and memory limits
- **Isolated workspace**: each compilation uses a unique temp directory
- **Error handling**: compilation errors are captured and returned to the user as structured feedback

---

## LLM Integration Pattern

### Provider
- OpenAI API (GPT-4o by default, configurable via `OPENAI_MODEL`)

### Tailoring Flow
1. API reads the master resume content (`.tex` source or `.docx` extracted text)
2. Constructs a prompt with the resume content + job description + action type
3. Sends to OpenAI API
4. Parses the response and writes the tailored output
5. For `.tex`: compiles via LaTeX sandbox → PDF
6. For `.docx`: writes modified content back to a `.docx` file
7. For cover letter: generates a `.docx` or `.txt` file

### Prompt Engineering
- System prompt defines the tailoring objective and constraints
- User prompt provides the resume content and job description
- Output format is specified per action type
- Structure preservation is emphasized in prompts

---

## Observability

- Log important failures (auth, uploads, LLM calls, LaTeX compilation)
- Log startup success/failure
- Log request-level errors safely (no secrets in logs)
- Structured logging via Python's logging module

---

## Performance Guidance

- No premature optimization
- LLM calls and LaTeX compilation are the known slow paths
- Architecture supports future async job queue if needed (e.g., Celery/Redis)
- File I/O is contained in the services layer for easy caching later

---

## Security Guidance

- Never hardcode secrets
- Validate inputs at all boundaries
- Restrict privileged operations to authenticated users
- Keep configuration explicit via `.env`
- Uploaded files are validated for type and size
- LaTeX compilation is sandboxed
- Generated filenames are sanitized

---

## Known Gaps (to be addressed in future milestones)
- Alembic migrations not yet configured
- Background job queue not yet needed
- Rate limiting not yet implemented
- S3 storage adapter not yet built
- Monitoring/alerting not yet configured