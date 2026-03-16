"""Business operations for Master Resumes."""

import uuid

from fastapi import HTTPException, UploadFile, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.models.master_resume import MasterResume
from app.schemas.resume import ResumeUpdateRequest
from app.services.file_service import FileService, FileServiceError

file_service = FileService()


async def upload_resume(
    db: AsyncSession,
    user_id: uuid.UUID,
    file: UploadFile,
    display_name: str | None = None
) -> MasterResume:
    """Upload and create a new master resume."""
    
    # 1. Validate file size explicitly
    file.file.seek(0, 2)
    file_size = file.file.tell()
    file.file.seek(0)
    
    max_size = settings.max_upload_size_mb * 1024 * 1024
    if file_size > max_size:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"File size exceeds maximum limit of {settings.max_upload_size_mb}MB"
        )

    # 2. Save it down using the secure file service
    try:
        storage_path, file_format, _ = await file_service.save_upload(user_id, file)
    except FileServiceError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
        
    # 3. Create database record
    effective_display_name = display_name if display_name else file.filename
    resume = MasterResume(
        user_id=user_id,
        filename=file.filename,
        format=file_format,
        storage_path=storage_path,
        display_name=effective_display_name
    )
    
    db.add(resume)
    await db.commit()
    await db.refresh(resume)
    return resume


async def get_resumes(db: AsyncSession, user_id: uuid.UUID) -> list[MasterResume]:
    """Retrieve all resumes specific to a user."""
    result = await db.execute(
        select(MasterResume)
        .where(MasterResume.user_id == user_id)
        .order_by(MasterResume.created_at.desc())
    )
    return list(result.scalars().all())


async def get_resume(db: AsyncSession, user_id: uuid.UUID, resume_id: uuid.UUID) -> MasterResume:
    """Retrieve a specific resume ensuring owner isolation."""
    result = await db.execute(
        select(MasterResume)
        .where(MasterResume.user_id == user_id, MasterResume.id == resume_id)
    )
    resume = result.scalar_one_or_none()
    if not resume:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Resume not found"
        )
    return resume


async def update_resume(
    db: AsyncSession,
    user_id: uuid.UUID,
    resume_id: uuid.UUID,
    update_data: ResumeUpdateRequest
) -> MasterResume:
    """Update metadata for an existing resume."""
    resume = await get_resume(db, user_id, resume_id)
    
    if update_data.display_name is not None:
        resume.display_name = update_data.display_name
        
    await db.commit()
    await db.refresh(resume)
    return resume


async def delete_resume(db: AsyncSession, user_id: uuid.UUID, resume_id: uuid.UUID) -> None:
    """Delete a resume and clean up local file storage."""
    resume = await get_resume(db, user_id, resume_id)
    
    # 1. Delete from filesystem isolated directory
    file_service.delete_file(resume.storage_path)
    
    # 2. Delete from database
    await db.delete(resume)
    await db.commit()
