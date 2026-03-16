import { useState, useRef } from "react";
import { Button } from "@/components/ui/Button";
import { Input } from "@/components/ui/Input";
import styles from "./UploadResumeModal.module.css";
import { ErrorMessage } from "../ui/ErrorMessage";

interface UploadResumeModalProps {
  isOpen: boolean;
  onClose: () => void;
  onUpload: (file: File, displayName: string) => Promise<void>;
}

const MAX_SIZE_MB = 10;
const MAX_SIZE_BYTES = MAX_SIZE_MB * 1024 * 1024;
const ALLOWED_TYPES = [
  "application/vnd.openxmlformats-officedocument.wordprocessingml.document", // .docx
  "application/x-tex", // .tex (sometimes sent as text/plain or application/x-tex)
  "text/plain", // .tex fallback
  "application/pdf", // .pdf
];

export function UploadResumeModal({ isOpen, onClose, onUpload }: UploadResumeModalProps) {
  const [file, setFile] = useState<File | null>(null);
  const [displayName, setDisplayName] = useState("");
  const [isUploading, setIsUploading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  if (!isOpen) return null;

  const resetState = () => {
    setFile(null);
    setDisplayName("");
    setError(null);
  };

  const handleClose = () => {
    if (isUploading) return;
    resetState();
    onClose();
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setError(null);
    const selected = e.target.files?.[0];
    if (!selected) return;

    // Validate size
    if (selected.size > MAX_SIZE_BYTES) {
      setError(`File size exceeds the ${MAX_SIZE_MB}MB limit.`);
      return;
    }

    // Validate extension manually alongside MIME type for safety
    const ext = selected.name.split('.').pop()?.toLowerCase();
    if (ext !== "tex" && ext !== "docx" && ext !== "pdf") {
       setError("Only .tex, .docx, and .pdf files are allowed.");
       return;
    }

    setFile(selected);
    if (!displayName) {
      setDisplayName(selected.name.replace(/\.(tex|docx|pdf)$/i, ""));
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!file) return;

    try {
      setIsUploading(true);
      setError(null);
      await onUpload(file, displayName);
      handleClose();
    } catch (err: any) {
      setError(err.message || "Failed to upload file");
      setIsUploading(false);
    }
  };

  return (
    <div className={styles.overlay} onClick={handleClose}>
      <div className={styles.modal} onClick={(e) => e.stopPropagation()}>
        <div className={styles.header}>
          <h2 className={styles.title}>Upload Master Resume</h2>
          <button className={styles.closeBtn} onClick={handleClose} disabled={isUploading}>
            &times;
          </button>
        </div>

        <form onSubmit={handleSubmit} className={styles.form}>
          <div className={styles.dropzone}>
            <input
              type="file"
              ref={fileInputRef}
              onChange={handleFileChange}
              className={styles.fileInput}
              accept=".tex,.docx,.pdf"
              disabled={isUploading}
            />
            {!file ? (
              <div className={styles.dropzoneContent} onClick={() => fileInputRef.current?.click()}>
                <span className={styles.uploadIcon}>📤</span>
                <p>Click to select a .tex, .docx, or .pdf file</p>
                <span className={styles.subtext}>Max size: 10MB</span>
              </div>
            ) : (
              <div className={styles.selectedFile}>
                <span className={styles.fileIcon}>
                  {file.name.endsWith(".tex") ? "📝" : file.name.endsWith(".pdf") ? "📕" : "📄"}
                </span>
                <span className={styles.fileName}>{file.name}</span>
                <button
                  type="button"
                  className={styles.removeFileBtn}
                  onClick={() => setFile(null)}
                  disabled={isUploading}
                >
                  &times;
                </button>
              </div>
            )}
          </div>

          <div className={styles.inputGroup}>
            <label htmlFor="displayName" className={styles.label}>
              Display Name (Optional)
            </label>
            <Input
              id="displayName"
              placeholder="e.g., Software Engineer Standard"
              value={displayName}
              onChange={(e) => setDisplayName(e.target.value)}
              disabled={isUploading}
            />
          </div>

          {error && <div className={styles.error}>{error}</div>}

          <div className={styles.footer}>
            <Button
              type="button"
              variant="secondary"
              onClick={handleClose}
              disabled={isUploading}
            >
              Cancel
            </Button>
            <Button
              type="submit"
              variant="primary"
              disabled={!file || isUploading}
              loading={isUploading}
            >
              {isUploading ? "Uploading..." : "Upload"}
            </Button>
          </div>
        </form>
      </div>
    </div>
  );
}
