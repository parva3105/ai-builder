"use client";

import Link from "next/link";
import { useAuth } from "@/contexts/AuthContext";
import { ProtectedRoute } from "@/components/ProtectedRoute";
import styles from "./page.module.css";

function DashboardContent() {
  const { user } = useAuth();

  const firstName = user?.full_name?.split(" ")[0] ?? "there";

  return (
    <div className={styles.dashboardPage}>
      <div className={styles.greeting}>
        <h1 className={styles.greetingTitle}>
          Welcome back, {firstName} 👋
        </h1>
        <p className={styles.greetingSubtitle}>
          Here&apos;s your resume tailoring workspace.
        </p>
      </div>

      <div className={styles.cardGrid}>
        <Link href="/resumes" className={styles.card} style={{ textDecoration: 'none', color: 'inherit' }}>
          <div className={styles.cardIcon}>📄</div>
          <h2 className={styles.cardTitle}>My Resumes</h2>
          <p className={styles.cardDescription}>
            Upload and manage your master resumes in LaTeX, DOCX, or PDF format.
            Keep multiple versions for different roles.
          </p>
        </Link>

        <div className={styles.card}>
          <div className={styles.cardIcon}>🎯</div>
          <h2 className={styles.cardTitle}>Tailor Resume</h2>
          <p className={styles.cardDescription}>
            Paste a job description and let AI tailor your resume to
            highlight the most relevant skills and experience.
          </p>
          <span className={styles.cardBadge}>Coming in M4</span>
        </div>

        <div className={styles.card}>
          <div className={styles.cardIcon}>✉️</div>
          <h2 className={styles.cardTitle}>Cover Letters</h2>
          <p className={styles.cardDescription}>
            Generate personalized cover letters that complement your
            tailored resume for each application.
          </p>
          <span className={styles.cardBadge}>Coming in M4</span>
        </div>

        <div className={styles.card}>
          <div className={styles.cardIcon}>📥</div>
          <h2 className={styles.cardTitle}>Downloads</h2>
          <p className={styles.cardDescription}>
            Access your generated outputs — tailored resumes and cover
            letters ready for download.
          </p>
          <span className={styles.cardBadge}>Coming in M5</span>
        </div>
      </div>
    </div>
  );
}

export default function DashboardPage() {
  return (
    <ProtectedRoute>
      <DashboardContent />
    </ProtectedRoute>
  );
}
