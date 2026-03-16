/**
 * Shared TypeScript interfaces matching openapi.yaml schemas.
 * These are used by components, contexts, and pages for type safety.
 */

// ── Auth ─────────────────────────────────────────────────────

export interface RegisterRequest {
  email: string;
  password: string;
  full_name: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RefreshRequest {
  refresh_token: string;
}

export interface TokenResponse {
  access_token: string;
  refresh_token: string;
  token_type: string;
}

export interface AccessTokenResponse {
  access_token: string;
  token_type: string;
}

export interface UserProfile {
  id: string;
  email: string;
  full_name: string;
  created_at: string;
}

// ── Error ────────────────────────────────────────────────────

export interface ApiError {
  error: string;
  message?: string;
}

// ── Resumes ──────────────────────────────────────────────────

export interface ResumeItem {
  id: string;
  filename: string;
  format: "tex" | "docx";
  display_name: string;
  created_at: string;
}

export interface ResumeListResponse {
  items: ResumeItem[];
}

export interface ResumeUploadResponse {
  id: string;
  filename: string;
  format: "tex" | "docx";
  display_name: string;
  created_at: string;
}

export interface ResumeUpdateRequest {
  display_name?: string;
}

// ── Tailoring ────────────────────────────────────────────────

export type TailoringAction = "tailor_tex" | "tailor_docx" | "cover_letter";

export type TailoringRequestStatus =
  | "pending"
  | "processing"
  | "completed"
  | "failed";

export interface CreateTailoringRequest {
  resume_id: string;
  job_description: string;
  action: TailoringAction;
}

export interface TailoringRequestResponse {
  id: string;
  resume_id: string;
  action: TailoringAction;
  status: TailoringRequestStatus;
  error_message?: string | null;
  output_id?: string | null;
  created_at: string;
  completed_at?: string | null;
}

// ── Outputs ──────────────────────────────────────────────────

export type OutputFormat = "pdf" | "docx" | "txt";

export interface OutputItem {
  id: string;
  request_id: string;
  filename: string;
  format: OutputFormat;
  created_at: string;
}

// ── System ───────────────────────────────────────────────────

export interface HealthStatus {
  status: string;
  service: string;
  version?: string;
}
