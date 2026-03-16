"""Pydantic schemas for master resumes."""

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.models.master_resume import ResumeFormat


class ResumeItem(BaseModel):
    """Schema for a single master resume."""

    id: UUID
    filename: str
    format: ResumeFormat
    display_name: str
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ResumeListResponse(BaseModel):
    """Schema for listing multiple master resumes."""

    items: list[ResumeItem]


class ResumeUploadResponse(ResumeItem):
    """Schema for a successfully uploaded master resume."""
    pass


class ResumeUpdateRequest(BaseModel):
    """Request schema for updating a master resume."""

    display_name: str | None = Field(default=None, max_length=256)
