# Local Development Setup

## Prerequisites
- Python 3.11+
- Node.js 20+
- Docker & Docker Compose
- Git

## Quick Start

### 1. Clone and enter the repo
```bash
git clone <repo-url>
cd Project3
```

### 2. Copy environment file
```bash
cp .env.example .env
# Edit .env with your actual values (especially OPENAI_API_KEY)
```

### 3. Start infrastructure (database)
```bash
docker compose up -d db
```

### 4. Backend setup
```bash
cd apps/api
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload --port 8000
```

### 5. Frontend setup
```bash
cd apps/web
npm install
npm run dev
```

### 6. Verify
- Backend health: http://localhost:8000/health
- Frontend: http://localhost:3001

## Docker Compose (full stack)
```bash
docker compose up --build
```
This starts: PostgreSQL, FastAPI backend, Next.js frontend, and a LaTeX sandbox container.

## Running Tests

### Backend
```bash
cd apps/api
pytest ../../tests/backend/ -v
```

### Frontend
```bash
cd apps/web
npm test
```

## Common Issues
- If the database won't start, check that port 5432 is free.
- If the API fails to connect to the DB, ensure `DATABASE_URL` in `.env` points to the right host (`localhost` for local dev, `db` for Docker Compose).
