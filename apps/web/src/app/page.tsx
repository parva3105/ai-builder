"use client";

import Link from "next/link";
import { useAuth } from "@/contexts/AuthContext";
import { useRouter } from "next/navigation";
import { useEffect } from "react";
import styles from "./home.module.css";

export default function HomePage() {
  const { isAuthenticated, isLoading } = useAuth();
  const router = useRouter();

  useEffect(() => {
    if (!isLoading && isAuthenticated) {
      router.replace("/dashboard");
    }
  }, [isLoading, isAuthenticated, router]);

  return (
    <div className={styles.hero}>
      {/* Background gradient orbs */}
      <div className={styles.bgOrb1} aria-hidden="true" />
      <div className={styles.bgOrb2} aria-hidden="true" />
      <div className={styles.bgOrb3} aria-hidden="true" />

      <div className={styles.heroContent}>
        <div className={styles.badge}>
          <span className={styles.badgeDot} />
          AI-Powered Resume Tailoring
        </div>

        <h1 className={styles.title}>
          Land your dream job with{" "}
          <span className={styles.titleGradient}>perfectly tailored</span>{" "}
          resumes
        </h1>

        <p className={styles.subtitle}>
          Upload your master resume, paste a job description, and let AI create
          a tailored resume and cover letter that highlights exactly what
          employers want to see.
        </p>

        <div className={styles.ctas}>
          <Link href="/signup" className={styles.ctaPrimary} id="hero-get-started">
            Get Started Free
            <span className={styles.ctaArrow}>→</span>
          </Link>
          <Link href="/login" className={styles.ctaSecondary} id="hero-login">
            Log in
          </Link>
        </div>

        <div className={styles.features}>
          <div className={styles.feature}>
            <span className={styles.featureIcon}>📄</span>
            <div>
              <h3 className={styles.featureTitle}>LaTeX & DOCX</h3>
              <p className={styles.featureDesc}>
                Preserve your formatting perfectly
              </p>
            </div>
          </div>
          <div className={styles.feature}>
            <span className={styles.featureIcon}>🎯</span>
            <div>
              <h3 className={styles.featureTitle}>Job-Matched</h3>
              <p className={styles.featureDesc}>
                Tailored to each job description
              </p>
            </div>
          </div>
          <div className={styles.feature}>
            <span className={styles.featureIcon}>✉️</span>
            <div>
              <h3 className={styles.featureTitle}>Cover Letters</h3>
              <p className={styles.featureDesc}>
                Auto-generated and personalized
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
