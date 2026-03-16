"""GeneratedOutput ORM model."""

import enum
import uuid
from datetime import datetime

from sqlalchemy import ForeignKey, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class OutputFormat(str, enum.Enum):
    """Allowed generated output formats."""

    PDF = "pdf"
    DOCX = "docx"
    TXT = "txt"


class GeneratedOutput(Base):
    """A generated output file (tailored resume or cover letter)."""

    __tablename__ = "generated_outputs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    request_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tailoring_requests.id", ondelete="CASCADE"),
        nullable=False,
        unique=True,
        index=True,
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    filename: Mapped[str] = mapped_column(String(512), nullable=False)
    format: Mapped[OutputFormat] = mapped_column(nullable=False)
    storage_path: Mapped[str] = mapped_column(String(1024), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now()
    )

    # Relationships
    request: Mapped["TailoringRequest"] = relationship(back_populates="output")  # noqa: F821
    owner: Mapped["User"] = relationship(back_populates="outputs")  # noqa: F821
