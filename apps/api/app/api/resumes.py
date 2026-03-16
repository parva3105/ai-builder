"""Resumes API endpoints."""

import uuid
from typing import Annotated

from fastapi import APIRouter, Depends, Form, UploadFile, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.resume import (
    ResumeItem,
    ResumeListResponse,
    ResumeUpdateRequest,
    ResumeUploadResponse,
)
from app.services import resume_service

router = APIRouter()

# Dependency aliases for clean signatures
DbSession = Annotated[AsyncSession, Depends(get_db)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post("/upload", response_model=ResumeUploadResponse, status_code=status.HTTP_201_CREATED)
async def upload_resume(
    file: UploadFile,
    db: DbSession,
    current_user: CurrentUser,
    display_name: str | None = Form(None)
) -> ResumeUploadResponse:
    """Upload a new master resume (.tex, .docx, or .pdf)."""
    return await resume_service.upload_resume(  # type: ignore
        db=db,
        user_id=current_user.id,
        file=file,
        display_name=display_name
    )


@router.get("", response_model=ResumeListResponse)
async def list_resumes(
    db: DbSession,
    current_user: CurrentUser
) -> ResumeListResponse:
    """List all master resumes owned by the authenticated user."""
    items = await resume_service.get_resumes(db, user_id=current_user.id)
    return ResumeListResponse(items=items)  # type: ignore


@router.get("/{resume_id}", response_model=ResumeItem)
async def get_resume(
    resume_id: uuid.UUID,
    db: DbSession,
    current_user: CurrentUser
) -> ResumeItem:
    """Get metadata for a specific master resume."""
    return await resume_service.get_resume(db, user_id=current_user.id, resume_id=resume_id)  # type: ignore


@router.patch("/{resume_id}", response_model=ResumeItem)
async def update_resume(
    resume_id: uuid.UUID,
    update_data: ResumeUpdateRequest,
    db: DbSession,
    current_user: CurrentUser
) -> ResumeItem:
    """Update metadata for an existing resume."""
    return await resume_service.update_resume(  # type: ignore
        db=db,
        user_id=current_user.id,
        resume_id=resume_id,
        update_data=update_data
    )


@router.delete("/{resume_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_resume(
    resume_id: uuid.UUID,
    db: DbSession,
    current_user: CurrentUser
) -> None:
    """Delete a master resume completely from db and filesystem."""
    await resume_service.delete_resume(db, user_id=current_user.id, resume_id=resume_id)
