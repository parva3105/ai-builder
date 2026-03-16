"""File storage service for handling resume uploads locally securely."""

import uuid
from pathlib import Path

from fastapi import UploadFile

from app.core.config import settings
from app.models.master_resume import ResumeFormat


class FileServiceError(Exception):
    """Base exception for file service errors."""
    pass


class FileService:
    """Handles secure file storage and retrieval for user uploads."""

    def __init__(self, upload_dir: str = settings.upload_dir):
        # We ensure the base upload directory exists upon instantiation
        self.upload_dir = Path(upload_dir)
        self.upload_dir.mkdir(parents=True, exist_ok=True)

    def _get_user_dir(self, user_id: uuid.UUID) -> Path:
        """Return the secure isolated directory for a specific user's resumes."""
        user_dir = self.upload_dir / str(user_id) / "resumes"
        user_dir.mkdir(parents=True, exist_ok=True)
        return user_dir

    def get_extension(self, filename: str) -> ResumeFormat:
        """Extract and validate the file extension."""
        ext = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""
        if ext == "tex":
            return ResumeFormat.TEX
        elif ext == "docx":
            return ResumeFormat.DOCX
        elif ext == "pdf":
            return ResumeFormat.PDF
        raise FileServiceError(f"Unsupported file format: {ext}")

    async def save_upload(self, user_id: uuid.UUID, file: UploadFile) -> tuple[str, ResumeFormat, int]:
        """
        Save an uploaded file safely to disk.
        Returns the (relative_storage_path, format, size_bytes).
        """
        if not file.filename:
            raise FileServiceError("Filename is missing")
            
        file_format = self.get_extension(file.filename)
        user_dir = self._get_user_dir(user_id)
        
        # Generate a secure randomized filename to prevent overwrites or traversal
        secure_filename = f"{uuid.uuid4()}.{file_format.value}"
        file_path = user_dir / secure_filename
        
        # Safely stream the file to disk in chunks
        size_bytes = 0
        try:
            with file_path.open("wb") as buffer:
                while chunk := await file.read(1024 * 1024):  # 1MB chunks
                    size_bytes += len(chunk)
                    buffer.write(chunk)
        except Exception as e:
            if file_path.exists():
                file_path.unlink()
            raise FileServiceError(f"Failed to save file: {str(e)}") from e
            
        # Return relative storage path for DB storage (e.g. "{user_id}/resumes/{uuid}.tex")
        relative_path = Path(str(user_id)) / "resumes" / secure_filename
        # Normalize to forward slashes for cross-platform DB compatibility
        return str(relative_path).replace("\\", "/"), file_format, size_bytes

    def delete_file(self, relative_path: str) -> bool:
        """Delete a file by its relative path. Returns True if deleted."""
        # Sanity check to prevent directory traversal out of upload_dir
        if ".." in relative_path or relative_path.startswith("/"):
            return False
            
        file_path = self.upload_dir / relative_path
        if file_path.exists() and file_path.is_file():
            # Ensures we are deleting a file within the upload directory
            if self.upload_dir in file_path.parents:
                file_path.unlink()
                return True
        return False
