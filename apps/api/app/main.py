"""TailorFlow API – FastAPI application entry point."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.resumes import router as resumes_router
from app.core.config import settings

app = FastAPI(
    title="TailorFlow API",
    version="0.1.0",
    description="AI-powered resume tailoring and cover letter generation API.",
)

# ── CORS ─────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routers ──────────────────────────────────────────────────
app.include_router(auth_router)
app.include_router(resumes_router, prefix="/resumes", tags=["resumes"])


# ── Health ───────────────────────────────────────────────────
@app.get("/health", tags=["system"])
async def health_check() -> dict[str, str]:
    """Return service health status."""
    return {"status": "ok", "service": "tailorflow-api", "version": "0.1.0"}
