import type { ReactNode } from "react";
import { Button } from "./Button";
import styles from "./ui.module.css";

interface EmptyStateProps {
  icon?: string;
  title: string;
  description?: string;
  action?: {
    label: string;
    onClick: () => void;
  };
  children?: ReactNode;
}

export function EmptyState({
  icon = "📭",
  title,
  description,
  action,
  children,
}: EmptyStateProps) {
  return (
    <div className={styles.emptyContainer}>
      <div className={styles.emptyIcon} aria-hidden="true">
        {icon}
      </div>
      <h3 className={styles.emptyTitle}>{title}</h3>
      {description && (
        <p className={styles.emptyDescription}>{description}</p>
      )}
      {action && (
        <Button variant="primary" size="md" onClick={action.onClick}>
          {action.label}
        </Button>
      )}
      {children}
    </div>
  );
}
