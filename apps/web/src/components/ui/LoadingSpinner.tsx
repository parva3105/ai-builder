import styles from "./ui.module.css";

type SpinnerSize = "sm" | "md" | "lg";

interface LoadingSpinnerProps {
  size?: SpinnerSize;
  label?: string;
}

const sizeClass: Record<SpinnerSize, string> = {
  sm: styles.spinnerSm,
  md: styles.spinnerMd,
  lg: styles.spinnerLg,
};

export function LoadingSpinner({ size = "md", label }: LoadingSpinnerProps) {
  return (
    <div className={styles.spinnerContainer} role="status" aria-label={label ?? "Loading"}>
      <div className={`${styles.spinner} ${sizeClass[size]}`} />
      {label && <span className={styles.spinnerLabel}>{label}</span>}
    </div>
  );
}
