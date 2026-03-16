"""Unit tests for the auth service layer."""

import pytest
from app.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password,
)
from app.schemas.auth import RegisterRequest, LoginRequest
from app.services.auth_service import (
    authenticate_user,
    refresh_access_token,
    register_user,
)
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession


# ── Password hashing ────────────────────────────────────────
class TestPasswordHashing:
    def test_hash_password_returns_bcrypt_string(self) -> None:
        hashed = hash_password("testpassword123")
        assert hashed.startswith("$2")
        assert len(hashed) > 50

    def test_verify_password_correct(self) -> None:
        hashed = hash_password("securepwd")
        assert verify_password("securepwd", hashed) is True

    def test_verify_password_incorrect(self) -> None:
        hashed = hash_password("securepwd")
        assert verify_password("wrongpwd", hashed) is False


# ── Token creation / decoding ────────────────────────────────
class TestTokens:
    def test_access_token_round_trip(self) -> None:
        token = create_access_token("user-123")
        payload = decode_token(token)
        assert payload["sub"] == "user-123"
        assert payload["type"] == "access"

    def test_refresh_token_round_trip(self) -> None:
        token = create_refresh_token("user-456")
        payload = decode_token(token)
        assert payload["sub"] == "user-456"
        assert payload["type"] == "refresh"

    def test_decode_invalid_token_raises(self) -> None:
        from jose import JWTError
        with pytest.raises(JWTError):
            decode_token("invalid.token.value")


# ── Register service ─────────────────────────────────────────
class TestRegisterService:
    @pytest.mark.asyncio
    async def test_register_user_success(self, db_session: AsyncSession) -> None:
        data = RegisterRequest(email="new@example.com", password="password123", full_name="New User")
        result = await register_user(db_session, data)
        assert result.access_token
        assert result.refresh_token
        assert result.token_type == "bearer"

    @pytest.mark.asyncio
    async def test_register_duplicate_email_raises_409(self, db_session: AsyncSession) -> None:
        data = RegisterRequest(email="dup@example.com", password="password123", full_name="First")
        await register_user(db_session, data)
        await db_session.commit()

        with pytest.raises(HTTPException) as exc_info:
            await register_user(db_session, data)
        assert exc_info.value.status_code == 409


# ── Authenticate service ────────────────────────────────────
class TestAuthenticateService:
    @pytest.mark.asyncio
    async def test_authenticate_user_success(self, db_session: AsyncSession) -> None:
        reg = RegisterRequest(email="auth@test.com", password="password123", full_name="Auth User")
        await register_user(db_session, reg)
        await db_session.commit()

        login = LoginRequest(email="auth@test.com", password="password123")
        result = await authenticate_user(db_session, login)
        assert result.access_token
        assert result.refresh_token

    @pytest.mark.asyncio
    async def test_authenticate_bad_password_raises_401(self, db_session: AsyncSession) -> None:
        reg = RegisterRequest(email="bad@test.com", password="password123", full_name="Bad User")
        await register_user(db_session, reg)
        await db_session.commit()

        login = LoginRequest(email="bad@test.com", password="wrongpassword")
        with pytest.raises(HTTPException) as exc_info:
            await authenticate_user(db_session, login)
        assert exc_info.value.status_code == 401

    @pytest.mark.asyncio
    async def test_authenticate_nonexistent_email_raises_401(self, db_session: AsyncSession) -> None:
        login = LoginRequest(email="ghost@test.com", password="password123")
        with pytest.raises(HTTPException) as exc_info:
            await authenticate_user(db_session, login)
        assert exc_info.value.status_code == 401


# ── Refresh service ──────────────────────────────────────────
class TestRefreshService:
    def test_refresh_valid_token(self) -> None:
        refresh = create_refresh_token("user-999")
        result = refresh_access_token(refresh)
        assert result.access_token
        assert result.token_type == "bearer"

    def test_refresh_with_access_token_raises_401(self) -> None:
        access = create_access_token("user-999")
        with pytest.raises(HTTPException) as exc_info:
            refresh_access_token(access)
        assert exc_info.value.status_code == 401

    def test_refresh_invalid_token_raises_401(self) -> None:
        with pytest.raises(HTTPException) as exc_info:
            refresh_access_token("garbage.token.here")
        assert exc_info.value.status_code == 401
