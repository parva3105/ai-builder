"use client";

import Link from "next/link";
import { useAuth } from "@/contexts/AuthContext";
import { useRouter } from "next/navigation";
import { useState } from "react";
import styles from "./Navbar.module.css";

export function Navbar() {
  const { isAuthenticated, user, logout, isLoading } = useAuth();
  const router = useRouter();
  const [menuOpen, setMenuOpen] = useState(false);

  const handleLogout = () => {
    logout();
    setMenuOpen(false);
    router.push("/login");
  };

  const closeMenu = () => setMenuOpen(false);

  return (
    <>
      <nav className={styles.navbar} role="navigation" aria-label="Main navigation">
        <Link href="/" className={styles.brand}>
          <span className={styles.brandIcon}>TF</span>
          TailorFlow
        </Link>

        {/* Desktop navigation */}
        <div className={styles.desktopNav}>
          {isLoading ? null : isAuthenticated ? (
            <div className={styles.userSection}>
              <Link href="/dashboard" className={styles.navLink}>
                Dashboard
              </Link>
              <span className={styles.userName}>{user?.full_name}</span>
              <button
                onClick={handleLogout}
                className={styles.logoutBtn}
                id="nav-logout-btn"
              >
                Log out
              </button>
            </div>
          ) : (
            <>
              <Link href="/login" className={styles.navLink} id="nav-login-link">
                Log in
              </Link>
              <Link href="/signup" className={styles.navLinkPrimary} id="nav-signup-link">
                Get Started
              </Link>
            </>
          )}
        </div>

        {/* Mobile hamburger */}
        <button
          className={styles.hamburger}
          onClick={() => setMenuOpen(!menuOpen)}
          data-open={menuOpen}
          aria-label="Toggle menu"
          aria-expanded={menuOpen}
          id="nav-hamburger"
        >
          <span className={styles.hamburgerLine} />
          <span className={styles.hamburgerLine} />
          <span className={styles.hamburgerLine} />
        </button>
      </nav>

      {/* Mobile menu */}
      <div
        className={styles.mobileMenu}
        data-open={menuOpen}
        role="menu"
      >
        {isAuthenticated ? (
          <>
            <Link
              href="/dashboard"
              className={styles.navLink}
              onClick={closeMenu}
            >
              Dashboard
            </Link>
            <button
              onClick={handleLogout}
              className={styles.logoutBtn}
            >
              Log out
            </button>
          </>
        ) : (
          <>
            <Link
              href="/login"
              className={styles.navLink}
              onClick={closeMenu}
            >
              Log in
            </Link>
            <Link
              href="/signup"
              className={styles.navLink}
              onClick={closeMenu}
            >
              Sign up
            </Link>
          </>
        )}
      </div>
    </>
  );
}
