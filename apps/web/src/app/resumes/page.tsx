"use client";

import { useEffect, useState } from "react";
import { ProtectedRoute } from "@/components/ProtectedRoute";
import { useResumes } from "@/hooks/useResumes";
import { ResumeList } from "@/components/resumes/ResumeList";
import { UploadResumeModal } from "@/components/resumes/UploadResumeModal";
import { Button } from "@/components/ui/Button";
import { LoadingSpinner } from "@/components/ui/LoadingSpinner";
import { ErrorMessage } from "@/components/ui/ErrorMessage";
import styles from "./page.module.css";

function ResumesContent() {
  const {
    resumes,
    isLoading,
    error,
    fetchResumes,
    uploadResume,
    deleteResume,
    updateResume,
  } = useResumes();
  
  const [isUploadModalOpen, setIsUploadModalOpen] = useState(false);

  useEffect(() => {
    fetchResumes();
  }, [fetchResumes]);

  if (isLoading && resumes.length === 0) {
    return (
      <div className={styles.centerContainer}>
        <LoadingSpinner size="lg" label="Loading your resumes..." />
      </div>
    );
  }

  if (error && resumes.length === 0) {
    return (
      <div className={styles.centerContainer}>
        <ErrorMessage message={error} />
        <Button variant="secondary" onClick={() => fetchResumes()} className={styles.retryBtn}>
          Try Again
        </Button>
      </div>
    );
  }

  return (
    <div className={styles.page}>
      <header className={styles.header}>
        <div>
          <h1 className={styles.title}>My Resumes</h1>
          <p className={styles.subtitle}>
            Manage your master resumes in LaTeX, DOCX, or PDF format.
          </p>
        </div>
        <Button onClick={() => setIsUploadModalOpen(true)} variant="primary">
          <span className={styles.uploadIcon}>+</span> Upload Resume
        </Button>
      </header>

      <main className={styles.main}>
        <ResumeList
          resumes={resumes}
          onRename={updateResume}
          onDelete={deleteResume}
          onUploadClick={() => setIsUploadModalOpen(true)}
        />
      </main>

      <UploadResumeModal
        isOpen={isUploadModalOpen}
        onClose={() => setIsUploadModalOpen(false)}
        onUpload={uploadResume}
      />
    </div>
  );
}

export default function ResumesPage() {
  return (
    <ProtectedRoute>
      <ResumesContent />
    </ProtectedRoute>
  );
}
