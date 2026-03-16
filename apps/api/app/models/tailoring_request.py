"""TailoringRequest ORM model."""

import enum
import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class TailoringAction(str, enum.Enum):
    """Available tailoring actions."""

    TAILOR_TEX = "tailor_tex"
    TAILOR_DOCX = "tailor_docx"
    COVER_LETTER = "cover_letter"


class RequestStatus(str, enum.Enum):
    """Status of a tailoring request."""

    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"


class TailoringRequest(Base):
    """A user's request to tailor a resume or generate a cover letter."""

    __tablename__ = "tailoring_requests"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    resume_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("master_resumes.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    job_description: Mapped[str] = mapped_column(Text, nullable=False)
    action: Mapped[TailoringAction] = mapped_column(nullable=False)
    status: Mapped[RequestStatus] = mapped_column(
        nullable=False, default=RequestStatus.PENDING
    )
    error_message: Mapped[str | None] = mapped_column(String(2048), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now()
    )
    completed_at: Mapped[datetime | None] = mapped_column(nullable=True)

    # Relationships
    owner: Mapped["User"] = relationship(back_populates="tailoring_requests")  # noqa: F821
    resume: Mapped["MasterResume"] = relationship(back_populates="tailoring_requests")  # noqa: F821
    output: Mapped["GeneratedOutput | None"] = relationship(  # noqa: F821
        back_populates="request", uselist=False, cascade="all, delete-orphan"
    )
