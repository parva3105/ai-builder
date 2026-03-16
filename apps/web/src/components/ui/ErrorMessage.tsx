import { Button } from "./Button";
import styles from "./ui.module.css";

interface ErrorMessageProps {
  message: string;
  onRetry?: () => void;
}

export function ErrorMessage({ message, onRetry }: ErrorMessageProps) {
  return (
    <div className={styles.errorContainer} role="alert">
      <div className={styles.errorIcon} aria-hidden="true">⚠</div>
      <p className={styles.errorText}>{message}</p>
      {onRetry && (
        <Button variant="secondary" size="sm" onClick={onRetry}>
          Try again
        </Button>
      )}
    </div>
  );
}
