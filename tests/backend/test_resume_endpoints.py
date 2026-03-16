"""Integration tests for master resume endpoints."""

import uuid

import pytest
import pytest_asyncio
from httpx import AsyncClient


class TestResumeEndpoints:
    @pytest_asyncio.fixture
    async def auth_headers(self, client: AsyncClient) -> dict[str, str]:
        """Helper to create a test user and return auth headers."""
        email = f"test_{uuid.uuid4()}@example.com"
        await client.post(
            "/auth/register",
            json={"email": email, "password": "securepassword123", "full_name": "Test User"},
        )
        resp = await client.post(
            "/auth/login",
            json={"email": email, "password": "securepassword123"},
        )
        token = resp.json()["access_token"]
        return {"Authorization": f"Bearer {token}"}

    @pytest_asyncio.fixture
    async def other_auth_headers(self, client: AsyncClient) -> dict[str, str]:
        """Second user to verify cross-ownership isolation breaks."""
        email = f"other_{uuid.uuid4()}@example.com"
        await client.post(
            "/auth/register",
            json={"email": email, "password": "securepassword123", "full_name": "Other User"},
        )
        resp = await client.post(
            "/auth/login",
            json={"email": email, "password": "securepassword123"},
        )
        token = resp.json()["access_token"]
        return {"Authorization": f"Bearer {token}"}

    @pytest.mark.asyncio
    async def test_upload_resume_success(self, client: AsyncClient, auth_headers: dict[str, str]) -> None:
        file_content = b"Mock DOCX content"
        files = {
            "file": (
                "test_resume.docx",
                file_content,
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        }
        data = {"display_name": "My Primary Resume"}

        resp = await client.post("/resumes/upload", headers=auth_headers, data=data, files=files)
        assert resp.status_code == 201
        resp_data = resp.json()
        assert resp_data["filename"] == "test_resume.docx"
        assert resp_data["format"] == "docx"
        assert resp_data["display_name"] == "My Primary Resume"
        assert "id" in resp_data

    @pytest.mark.asyncio
    async def test_upload_resume_no_display_name(
        self, client: AsyncClient, auth_headers: dict[str, str]
    ) -> None:
        file_content = b"Mock TEX content"
        files = {"file": ("raw_resume.tex", file_content, "application/x-tex")}

        resp = await client.post("/resumes/upload", headers=auth_headers, files=files)
        assert resp.status_code == 201
        resp_data = resp.json()
        assert resp_data["filename"] == "raw_resume.tex"
        assert resp_data["format"] == "tex"
        assert resp_data["display_name"] == "raw_resume.tex"  # Defaults to filename

    @pytest.mark.asyncio
    async def test_upload_resume_pdf_success(
        self, client: AsyncClient, auth_headers: dict[str, str]
    ) -> None:
        files = {"file": ("test.pdf", b"pdf content", "application/pdf")}
        resp = await client.post("/resumes/upload", headers=auth_headers, files=files)
        assert resp.status_code == 201
        resp_data = resp.json()
        assert resp_data["filename"] == "test.pdf"
        assert resp_data["format"] == "pdf"

    @pytest.mark.asyncio
    async def test_upload_resume_unsupported_format(
        self, client: AsyncClient, auth_headers: dict[str, str]
    ) -> None:
        files = {"file": ("test.txt", b"text content", "text/plain")}
        resp = await client.post("/resumes/upload", headers=auth_headers, files=files)
        assert resp.status_code == 400
        assert "Unsupported file format" in str(resp.json())

    @pytest.mark.asyncio
    async def test_list_resumes(self, client: AsyncClient, auth_headers: dict[str, str]) -> None:
        files1 = {"file": ("resume1.tex", b"tex content", "application/x-tex")}
        await client.post(
            "/resumes/upload", headers=auth_headers, files=files1, data={"display_name": "R1"}
        )

        files2 = {
            "file": (
                "resume2.docx",
                b"docx content",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )
        }
        await client.post(
            "/resumes/upload", headers=auth_headers, files=files2, data={"display_name": "R2"}
        )

        resp = await client.get("/resumes", headers=auth_headers)
        assert resp.status_code == 200
        items = resp.json()["items"]
        assert len(items) == 2
        formats = {item["format"] for item in items}
        assert formats == {"tex", "docx"}

    @pytest.mark.asyncio
    async def test_get_and_update_resume(
        self, client: AsyncClient, auth_headers: dict[str, str], other_auth_headers: dict[str, str]
    ) -> None:
        files = {"file": ("test.tex", b"content", "application/x-tex")}
        upload_resp = await client.post(
            "/resumes/upload", headers=auth_headers, files=files, data={"display_name": "Old Name"}
        )
        resume_id = upload_resp.json()["id"]

        get_resp = await client.get(f"/resumes/{resume_id}", headers=auth_headers)
        assert get_resp.status_code == 200
        assert get_resp.json()["display_name"] == "Old Name"

        # Try to access from another user
        other_resp = await client.get(f"/resumes/{resume_id}", headers=other_auth_headers)
        assert other_resp.status_code == 404

        # Update it
        patch_resp = await client.patch(
            f"/resumes/{resume_id}", headers=auth_headers, json={"display_name": "New Name"}
        )
        assert patch_resp.status_code == 200
        assert patch_resp.json()["display_name"] == "New Name"

    @pytest.mark.asyncio
    async def test_delete_resume(self, client: AsyncClient, auth_headers: dict[str, str]) -> None:
        files = {"file": ("to_delete.tex", b"content", "application/x-tex")}
        upload_resp = await client.post("/resumes/upload", headers=auth_headers, files=files)
        resume_id = upload_resp.json()["id"]

        del_resp = await client.delete(f"/resumes/{resume_id}", headers=auth_headers)
        assert del_resp.status_code == 204

        # Verify it's gone
        get_resp = await client.get(f"/resumes/{resume_id}", headers=auth_headers)
        assert get_resp.status_code == 404
