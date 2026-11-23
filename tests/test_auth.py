"""Tests for the Auth Unificado backend.

Covers registration, login, token refresh, logout, profile, Google login
(with mocked Google service), API key enforcement and validation errors.
"""

import uuid
from unittest.mock import AsyncMock, patch

import pytest
from httpx import AsyncClient, ASGITransport

from src.core.database import get_db
from src.core.dependencies import verify_api_key
from src.core.security import require_admin, require_user
from src.main import app
from src.schemas.auth_dtos import UserLogin, UserRegister


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
async def auth_client(db):
    """Client with API key overridden but auth (JWT) NOT overridden."""

    async def override_get_db():
        yield db

    async def override_verify_api_key():
        return True

    app.dependency_overrides[get_db] = override_get_db
    app.dependency_overrides[verify_api_key] = override_verify_api_key
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()


@pytest.fixture
async def no_key_client(db):
    """Client WITHOUT API key override (to test X-API-Key enforcement)."""

    async def override_get_db():
        yield db

    app.dependency_overrides[get_db] = override_get_db
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

REGISTER_PAYLOAD = {
    "email": "test@example.com",
    "password": "password123",
    "name": "Test",
    "lastname": "User",
}

LOGIN_PAYLOAD = {
    "email": "test@example.com",
    "password": "password123",
}


async def _register(client, payload=None):
    return await client.post("/api/auth/register", json=payload or REGISTER_PAYLOAD)


async def _login(client, payload=None):
    return await client.post("/api/auth/login", json=payload or LOGIN_PAYLOAD)


# ---------------------------------------------------------------------------
# API Key enforcement
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_api_key_missing(no_key_client):
    resp = await no_key_client.post("/api/auth/register", json=REGISTER_PAYLOAD)
    assert resp.status_code == 401
    assert "api" in resp.json()["detail"].lower() or "key" in resp.json()["detail"].lower()


@pytest.mark.asyncio
async def test_api_key_invalid(no_key_client):
    resp = await no_key_client.post(
        "/api/auth/register",
        json=REGISTER_PAYLOAD,
        headers={"X-API-Key": "wrong-key"},
    )
    assert resp.status_code == 401


# ---------------------------------------------------------------------------
# Registration
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_register_success(auth_client):
    resp = await _register(auth_client)
    assert resp.status_code == 201
    data = resp.json()
    assert data["access_token"]
    assert data["refresh_token"]
    assert data["token_type"] == "bearer"
    assert data["expires_in"] == 900


@pytest.mark.asyncio
async def test_register_duplicate_email(auth_client):
    await _register(auth_client)
    resp = await _register(auth_client)
    assert resp.status_code == 409
    assert "registrado" in resp.json()["detail"].lower() or "exists" in resp.json()["detail"].lower()


@pytest.mark.asyncio
async def test_register_password_too_short(auth_client):
    payload = {**REGISTER_PAYLOAD, "password": "short"}
    resp = await _register(auth_client, payload)
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_register_invalid_email(auth_client):
    payload = {**REGISTER_PAYLOAD, "email": "not-an-email"}
    resp = await _register(auth_client, payload)
    assert resp.status_code == 422


# ---------------------------------------------------------------------------
# Login
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_login_success(auth_client):
    await _register(auth_client)
    resp = await _login(auth_client)
    assert resp.status_code == 200
    data = resp.json()
    assert data["access_token"]
    assert data["refresh_token"]


@pytest.mark.asyncio
async def test_login_wrong_password(auth_client):
    await _register(auth_client)
    resp = await _login(auth_client, {"email": "test@example.com", "password": "wrongpassword"})
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_login_nonexistent_user(auth_client):
    resp = await _login(auth_client, {"email": "nobody@example.com", "password": "password123"})
    assert resp.status_code == 401


# ---------------------------------------------------------------------------
# Profile (me)
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_me_without_auth(auth_client):
    resp = await auth_client.get("/api/auth/me")
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_me_with_valid_token(auth_client):
    reg = await _register(auth_client)
    token = reg.json()["access_token"]
    resp = await auth_client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["email"] == "test@example.com"
    assert data["name"] == "Test"
    assert data["role"] == "user"
    assert data["provider"] is None or data["provider"] == "local"


# ---------------------------------------------------------------------------
# Refresh token
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_refresh_success(auth_client):
    reg = await _register(auth_client)
    refresh_token = reg.json()["refresh_token"]
    resp = await auth_client.post("/api/auth/refresh", json={"refresh_token": refresh_token})
    assert resp.status_code == 200
    data = resp.json()
    assert data["access_token"]
    assert data["refresh_token"]
    # Rotated: new refresh token should differ
    assert data["refresh_token"] != refresh_token


@pytest.mark.asyncio
async def test_refresh_invalid_token(auth_client):
    resp = await auth_client.post("/api/auth/refresh", json={"refresh_token": "invalid-token"})
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_refresh_reuse_detection(auth_client):
    reg = await _register(auth_client)
    refresh_token = reg.json()["refresh_token"]
    # First refresh (rotates)
    resp1 = await auth_client.post("/api/auth/refresh", json={"refresh_token": refresh_token})
    assert resp1.status_code == 200
    # Reuse the old token → should be rejected and revoke all sessions
    resp2 = await auth_client.post("/api/auth/refresh", json={"refresh_token": refresh_token})
    assert resp2.status_code == 401
    assert "reuse" in resp2.json()["detail"].lower() or "revoked" in resp2.json()["detail"].lower()


# ---------------------------------------------------------------------------
# Logout
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_logout_without_auth(auth_client):
    resp = await auth_client.post("/api/auth/logout")
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_logout_success(auth_client):
    reg = await _register(auth_client)
    token = reg.json()["access_token"]
    resp = await auth_client.post("/api/auth/logout", headers={"Authorization": f"Bearer {token}"})
    assert resp.status_code == 200
    assert resp.json()["status"] == "logged_out"


# ---------------------------------------------------------------------------
# Google login
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_google_invalid_token(auth_client):
    resp = await auth_client.post("/api/auth/google", json={"googleToken": "invalid-token"})
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_google_missing_token(auth_client):
    resp = await auth_client.post("/api/auth/google", json={})
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_google_valid_token(auth_client, monkeypatch):
    # Mock google_service to return valid data
    mock_info = {
        "sub": "google-user-123",
        "email": "google@example.com",
        "email_verified": "true",
        "given_name": "Google",
        "family_name": "User",
        "picture": "https://example.com/pic.jpg",
    }
    mock_profile = {
        "given_name": "Google",
        "family_name": "User",
        "picture": "https://example.com/pic.jpg",
    }

    async def mock_verify(token):
        return mock_info

    async def mock_fetch(token):
        return mock_profile

    monkeypatch.setattr("src.api.auth.google_service.verify_google_token", mock_verify)
    monkeypatch.setattr("src.api.auth.google_service.fetch_google_userinfo", mock_fetch)

    resp = await auth_client.post("/api/auth/google", json={"googleToken": "fake-google-token"})
    assert resp.status_code == 201 or resp.status_code == 200
    data = resp.json()
    assert data["access_token"]
    assert data["refresh_token"]

    # Verify profile was created
    token = data["access_token"]
    profile_resp = await auth_client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert profile_resp.status_code == 200
    profile = profile_resp.json()
    assert profile["email"] == "google@example.com"
    assert profile["name"] == "Google"
    assert profile["provider"] == "google"


# ---------------------------------------------------------------------------
# GitHub login
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_github_invalid_token(auth_client):
    resp = await auth_client.post("/api/auth/github", json={"code": "invalid-code"})
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_github_missing_token(auth_client):
    resp = await auth_client.post("/api/auth/github", json={})
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_github_valid_token(auth_client, monkeypatch):
    mock_info = {
        "sub": "github-user-456",
        "email": "github@example.com",
        "email_verified": True,
        "given_name": "GitHub",
        "family_name": "User",
        "lastname": "User",
        "picture": "https://example.com/github-pic.jpg",
    }

    async def mock_exchange(code):
        return "fake-access-token"

    async def mock_verify(token):
        return mock_info

    async def mock_fetch(token):
        return mock_info

    monkeypatch.setattr("src.api.auth.github_service.exchange_code_for_token", mock_exchange)
    monkeypatch.setattr("src.api.auth.github_service.verify_github_token", mock_verify)
    monkeypatch.setattr("src.api.auth.github_service.fetch_github_userinfo", mock_fetch)

    resp = await auth_client.post("/api/auth/github", json={"code": "fake-auth-code"})
    assert resp.status_code in (200, 201)
    data = resp.json()
    assert data["access_token"]
    assert data["refresh_token"]

    token = data["access_token"]
    profile_resp = await auth_client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert profile_resp.status_code == 200
    profile = profile_resp.json()
    assert profile["email"] == "github@example.com"
    assert profile["provider"] == "github"


# ---------------------------------------------------------------------------
# Apple login
# ---------------------------------------------------------------------------

@pytest.mark.asyncio
async def test_apple_invalid_token(auth_client):
    resp = await auth_client.post("/api/auth/apple", json={"appleToken": "invalid-token"})
    assert resp.status_code == 401


@pytest.mark.asyncio
async def test_apple_missing_token(auth_client):
    resp = await auth_client.post("/api/auth/apple", json={})
    assert resp.status_code == 422


@pytest.mark.asyncio
async def test_apple_valid_token(auth_client, monkeypatch):
    mock_info = {
        "sub": "apple-user-789",
        "email": "apple@example.com",
        "email_verified": True,
        "given_name": None,
        "family_name": None,
        "lastname": None,
        "picture": None,
    }

    async def mock_verify(token):
        return mock_info

    async def mock_fetch(token):
        return mock_info

    monkeypatch.setattr("src.api.auth.apple_service.verify_apple_token", mock_verify)
    monkeypatch.setattr("src.api.auth.apple_service.fetch_apple_userinfo", mock_fetch)

    resp = await auth_client.post(
        "/api/auth/apple",
        json={"appleToken": "fake-apple-token", "name": "Apple", "lastname": "User"},
    )
    assert resp.status_code in (200, 201)
    data = resp.json()
    assert data["access_token"]
    assert data["refresh_token"]

    token = data["access_token"]
    profile_resp = await auth_client.get("/api/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert profile_resp.status_code == 200
    profile = profile_resp.json()
    assert profile["email"] == "apple@example.com"
    assert profile["name"] == "Apple"
    assert profile["provider"] == "apple"