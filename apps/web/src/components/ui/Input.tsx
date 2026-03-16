import { forwardRef, type InputHTMLAttributes } from "react";
import styles from "./ui.module.css";

interface InputProps extends InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
}

export const Input = forwardRef<HTMLInputElement, InputProps>(
  function Input({ label, error, id, className, ...rest }, ref) {
    const fieldClasses = [
      styles.inputField,
      error ? styles.inputFieldError : "",
      className,
    ]
      .filter(Boolean)
      .join(" ");

    return (
      <div className={styles.inputGroup}>
        {label && (
          <label htmlFor={id} className={styles.inputLabel}>
            {label}
          </label>
        )}
        <input ref={ref} id={id} className={fieldClasses} {...rest} />
        {error && <span className={styles.inputError} role="alert">{error}</span>}
      </div>
    );
  }
);
