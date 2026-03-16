"""MasterResume ORM model."""

import enum
import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class ResumeFormat(str, enum.Enum):
    """Allowed master resume file formats."""

    TEX = "tex"
    DOCX = "docx"


class MasterResume(Base):
    """An uploaded master resume owned by a user."""

    __tablename__ = "master_resumes"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    filename: Mapped[str] = mapped_column(String(512), nullable=False)
    format: Mapped[ResumeFormat] = mapped_column(nullable=False)
    storage_path: Mapped[str] = mapped_column(String(1024), nullable=False)
    display_name: Mapped[str] = mapped_column(String(256), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now()
    )

    # Relationships
    owner: Mapped["User"] = relationship(back_populates="resumes")  # noqa: F821
    tailoring_requests: Mapped[list["TailoringRequest"]] = relationship(  # noqa: F821
        back_populates="resume", cascade="all, delete-orphan"
    )
