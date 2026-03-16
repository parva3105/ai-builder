"""User ORM model."""

import uuid
from datetime import datetime, timezone

from sqlalchemy import String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):
    """Application user – owns resumes, requests, and outputs."""

    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(String(320), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    full_name: Mapped[str] = mapped_column(String(256), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        nullable=False, server_default=func.now(), onupdate=func.now()
    )

    # Relationships
    resumes: Mapped[list["MasterResume"]] = relationship(  # noqa: F821
        back_populates="owner", cascade="all, delete-orphan"
    )
    tailoring_requests: Mapped[list["TailoringRequest"]] = relationship(  # noqa: F821
        back_populates="owner", cascade="all, delete-orphan"
    )
    outputs: Mapped[list["GeneratedOutput"]] = relationship(  # noqa: F821
        back_populates="owner", cascade="all, delete-orphan"
    )
