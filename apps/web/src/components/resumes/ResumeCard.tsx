import { useState } from "react";
import { Resume } from "@/hooks/useResumes";
import { Input } from "@/components/ui/Input";
import { Button } from "@/components/ui/Button";
import styles from "./ResumeCard.module.css";

interface ResumeCardProps {
  resume: Resume;
  onRename: (id: string, newName: string) => Promise<any>;
  onDelete: (id: string) => Promise<void>;
}

export function ResumeCard({ resume, onRename, onDelete }: ResumeCardProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [editName, setEditName] = useState(resume.display_name);
  const [isUpdating, setIsUpdating] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);

  const handleSave = async () => {
    if (!editName.trim() || editName === resume.display_name) {
      setIsEditing(false);
      setEditName(resume.display_name);
      return;
    }
    setIsUpdating(true);
    await onRename(resume.id, editName);
    setIsUpdating(false);
    setIsEditing(false);
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") handleSave();
    if (e.key === "Escape") {
      setIsEditing(false);
      setEditName(resume.display_name);
    }
  };

  const handleDelete = async () => {
    if (confirm("Are you sure you want to delete this resume?")) {
      setIsDeleting(true);
      await onDelete(resume.id);
      setIsDeleting(false);
    }
  };

  const dateStr = new Date(resume.created_at).toLocaleDateString([], {
    year: "numeric",
    month: "short",
    day: "numeric",
  });

  return (
    <div className={styles.card}>
      <div className={styles.cardHeader}>
        <div className={styles.iconContainer}>
          <span className={styles.icon}>{resume.format === "tex" ? "📝" : resume.format === "pdf" ? "📕" : "📄"}</span>
        </div>
        <div className={styles.actions}>
          <button
            className={styles.iconBtn}
            onClick={() => setIsEditing(true)}
            aria-label="Rename resume"
            disabled={isUpdating || isDeleting}
          >
            ✏️
          </button>
          <button
            className={styles.iconBtn}
            onClick={handleDelete}
            aria-label="Delete resume"
            disabled={isUpdating || isDeleting}
          >
            🗑️
          </button>
        </div>
      </div>

      <div className={styles.cardBody}>
        {isEditing ? (
          <div className={styles.editMode}>
            <Input
              value={editName}
              onChange={(e) => setEditName(e.target.value)}
              onKeyDown={handleKeyDown}
              onBlur={handleSave}
              autoFocus
              disabled={isUpdating}
            />
          </div>
        ) : (
          <h3 className={styles.title} title={resume.display_name}>
            {resume.display_name}
          </h3>
        )}
        <p className={styles.filename} title={resume.filename}>
          {resume.filename}
        </p>
      </div>

      <div className={styles.cardFooter}>
        <span className={styles.badge}>{resume.format.toUpperCase()}</span>
        <span className={styles.date}>{dateStr}</span>
      </div>
    </div>
  );
}
