"""Integration tests for auth endpoints via the ASGI TestClient."""

import pytest
from httpx import AsyncClient


class TestRegisterEndpoint:
    @pytest.mark.asyncio
    async def test_register_success(self, client: AsyncClient) -> None:
        resp = await client.post("/auth/register", json={
            "email": "jane@example.com",
            "password": "securepassword123",
            "full_name": "Jane Doe",
        })
        assert resp.status_code == 201
        data = resp.json()
        assert "access_token" in data
        assert "refresh_token" in data
        assert data["token_type"] == "bearer"

    @pytest.mark.asyncio
    async def test_register_duplicate_email(self, client: AsyncClient) -> None:
        payload = {
            "email": "dup@example.com",
            "password": "securepassword123",
            "full_name": "First User",
        }
        resp1 = await client.post("/auth/register", json=payload)
        assert resp1.status_code == 201

        resp2 = await client.post("/auth/register", json=payload)
        assert resp2.status_code == 409

    @pytest.mark.asyncio
    async def test_register_short_password(self, client: AsyncClient) -> None:
        resp = await client.post("/auth/register", json={
            "email": "short@example.com",
            "password": "1234567",  # Only 7 chars
            "full_name": "Short Pwd",
        })
        assert resp.status_code == 422

    @pytest.mark.asyncio
    async def test_register_invalid_email(self, client: AsyncClient) -> None:
        resp = await client.post("/auth/register", json={
            "email": "not-an-email",
            "password": "securepassword123",
            "full_name": "Bad Email",
        })
        assert resp.status_code == 422


class TestLoginEndpoint:
    @pytest.mark.asyncio
    async def test_login_success(self, client: AsyncClient) -> None:
        # Register first
        await client.post("/auth/register", json={
            "email": "login@example.com",
            "password": "securepassword123",
            "full_name": "Login User",
        })

        resp = await client.post("/auth/login", json={
            "email": "login@example.com",
            "password": "securepassword123",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert "access_token" in data
        assert "refresh_token" in data

    @pytest.mark.asyncio
    async def test_login_wrong_password(self, client: AsyncClient) -> None:
        await client.post("/auth/register", json={
            "email": "wrongpw@example.com",
            "password": "securepassword123",
            "full_name": "Wrong PW",
        })

        resp = await client.post("/auth/login", json={
            "email": "wrongpw@example.com",
            "password": "wrongpassword",
        })
        assert resp.status_code == 401

    @pytest.mark.asyncio
    async def test_login_nonexistent_email(self, client: AsyncClient) -> None:
        resp = await client.post("/auth/login", json={
            "email": "ghost@example.com",
            "password": "securepassword123",
        })
        assert resp.status_code == 401


class TestRefreshEndpoint:
    @pytest.mark.asyncio
    async def test_refresh_success(self, client: AsyncClient) -> None:
        reg = await client.post("/auth/register", json={
            "email": "refresh@example.com",
            "password": "securepassword123",
            "full_name": "Refresh User",
        })
        refresh_token = reg.json()["refresh_token"]

        resp = await client.post("/auth/refresh", json={
            "refresh_token": refresh_token,
        })
        assert resp.status_code == 200
        data = resp.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"
        # Should not contain refresh_token in the response
        assert "refresh_token" not in data

    @pytest.mark.asyncio
    async def test_refresh_invalid_token(self, client: AsyncClient) -> None:
        resp = await client.post("/auth/refresh", json={
            "refresh_token": "invalid.token.here",
        })
        assert resp.status_code == 401

    @pytest.mark.asyncio
    async def test_refresh_with_access_token(self, client: AsyncClient) -> None:
        reg = await client.post("/auth/register", json={
            "email": "accref@example.com",
            "password": "securepassword123",
            "full_name": "Access Ref",
        })
        access_token = reg.json()["access_token"]

        resp = await client.post("/auth/refresh", json={
            "refresh_token": access_token,  # Wrong token type
        })
        assert resp.status_code == 401


class TestMeEndpoint:
    @pytest.mark.asyncio
    async def test_me_success(self, client: AsyncClient) -> None:
        reg = await client.post("/auth/register", json={
            "email": "me@example.com",
            "password": "securepassword123",
            "full_name": "Me User",
        })
        access_token = reg.json()["access_token"]

        resp = await client.get("/auth/me", headers={
            "Authorization": f"Bearer {access_token}",
        })
        assert resp.status_code == 200
        data = resp.json()
        assert data["email"] == "me@example.com"
        assert data["full_name"] == "Me User"
        assert "id" in data
        assert "created_at" in data

    @pytest.mark.asyncio
    async def test_me_no_auth(self, client: AsyncClient) -> None:
        resp = await client.get("/auth/me")
        assert resp.status_code == 403  # HTTPBearer returns 403 when no credentials

    @pytest.mark.asyncio
    async def test_me_invalid_token(self, client: AsyncClient) -> None:
        resp = await client.get("/auth/me", headers={
            "Authorization": "Bearer invalid.token.here",
        })
        assert resp.status_code == 401


class TestHealthEndpoint:
    @pytest.mark.asyncio
    async def test_health_returns_ok(self, client: AsyncClient) -> None:
        resp = await client.get("/health")
        assert resp.status_code == 200
        data = resp.json()
        assert data["status"] == "ok"
        assert data["service"] == "tailorflow-api"
