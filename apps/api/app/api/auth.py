"""Auth router – register, login, refresh, and current-user endpoints."""

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.auth import (
    AccessTokenResponse,
    LoginRequest,
    RefreshRequest,
    RegisterRequest,
    TokenResponse,
    UserProfile,
)
from app.services.auth_service import authenticate_user, refresh_access_token, register_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(data: RegisterRequest, db: AsyncSession = Depends(get_db)) -> TokenResponse:
    """Register a new user and return access + refresh tokens."""
    return await register_user(db, data)


@router.post("/login", response_model=TokenResponse)
async def login(data: LoginRequest, db: AsyncSession = Depends(get_db)) -> TokenResponse:
    """Log in with email and password."""
    return await authenticate_user(db, data)


@router.post("/refresh", response_model=AccessTokenResponse)
async def refresh(data: RefreshRequest) -> AccessTokenResponse:
    """Refresh access token using a valid refresh token."""
    return refresh_access_token(data.refresh_token)


@router.get("/me", response_model=UserProfile)
async def me(current_user: User = Depends(get_current_user)) -> UserProfile:
    """Get the profile of the currently authenticated user."""
    return UserProfile.model_validate(current_user)
