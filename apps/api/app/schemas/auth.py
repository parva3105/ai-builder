"""Pydantic request/response schemas for auth endpoints."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr, Field


# ── Requests ─────────────────────────────────────────────────
class RegisterRequest(BaseModel):
    """POST /auth/register request body."""

    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str


class LoginRequest(BaseModel):
    """POST /auth/login request body."""

    email: EmailStr
    password: str


class RefreshRequest(BaseModel):
    """POST /auth/refresh request body."""

    refresh_token: str


# ── Responses ────────────────────────────────────────────────
class TokenResponse(BaseModel):
    """Returned on register and login – both tokens."""

    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class AccessTokenResponse(BaseModel):
    """Returned on token refresh – access token only."""

    access_token: str
    token_type: str = "bearer"


class UserProfile(BaseModel):
    """GET /auth/me response – current user profile."""

    id: UUID
    email: str
    full_name: str
    created_at: datetime

    model_config = {"from_attributes": True}
