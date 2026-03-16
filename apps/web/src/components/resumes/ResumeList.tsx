import { Resume } from "@/hooks/useResumes";
import { ResumeCard } from "./ResumeCard";
import { EmptyState } from "@/components/ui/EmptyState";
import styles from "./ResumeList.module.css";

interface ResumeListProps {
  resumes: Resume[];
  onRename: (id: string, newName: string) => Promise<any>;
  onDelete: (id: string) => Promise<void>;
  onUploadClick: () => void;
}

export function ResumeList({ resumes, onRename, onDelete, onUploadClick }: ResumeListProps) {
  if (resumes.length === 0) {
    return (
      <EmptyState
        icon="📄"
        title="No resumes yet"
        description="Upload your master resume in .tex, .docx, or .pdf format to get started."
        action={{
          label: "Upload Resume",
          onClick: onUploadClick
        }}
      />
    );
  }

  return (
    <div className={styles.grid}>
      {resumes.map((resume) => (
        <ResumeCard
          key={resume.id}
          resume={resume}
          onRename={onRename}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}
