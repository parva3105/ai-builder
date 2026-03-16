/**
 * TailorFlow API client – typed fetch wrapper for the backend.
 */

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

/** Standard error response from the API. */
export interface ApiError {
  error: string;
  message?: string;
}

/** Generic fetch wrapper with error handling. */
async function apiFetch<T>(
  path: string,
  options: RequestInit = {}
): Promise<T> {
  const url = `${API_BASE_URL}${path}`;

  const headers: HeadersInit = {
    "Content-Type": "application/json",
    ...options.headers,
  };

  const res = await fetch(url, { ...options, headers });

  if (!res.ok) {
    const body: ApiError = await res.json().catch(() => ({
      error: "unknown",
      message: res.statusText,
    }));
    throw new Error(body.message ?? body.error);
  }

  return res.json() as Promise<T>;
}

/** Attach a JWT bearer token to requests. */
function authHeaders(token: string): HeadersInit {
  return { Authorization: `Bearer ${token}` };
}

// ── Public API methods ──────────────────────────────────────

export const api = {
  /** Health check */
  health: () => apiFetch<{ status: string; service: string; version: string }>("/health"),

  /** Auth */
  auth: {
    register: (email: string, password: string, fullName: string) =>
      apiFetch<{ access_token: string; refresh_token: string }>("/auth/register", {
        method: "POST",
        body: JSON.stringify({ email, password, full_name: fullName }),
      }),

    login: (email: string, password: string) =>
      apiFetch<{ access_token: string; refresh_token: string }>("/auth/login", {
        method: "POST",
        body: JSON.stringify({ email, password }),
      }),

    refresh: (refreshToken: string) =>
      apiFetch<{ access_token: string }>("/auth/refresh", {
        method: "POST",
        body: JSON.stringify({ refresh_token: refreshToken }),
      }),

    me: (token: string) =>
      apiFetch<{ id: string; email: string; full_name: string }>("/auth/me", {
        headers: authHeaders(token),
      }),
  },

  /** Resumes */
  resumes: {
    list: (token: string) =>
      apiFetch<{ items: Array<{ id: string; filename: string; format: string; created_at: string }> }>(
        "/resumes",
        { headers: authHeaders(token) }
      ),

    upload: async (token: string, file: File) => {
      const formData = new FormData();
      formData.append("file", file);
      const res = await fetch(`${API_BASE_URL}/resumes/upload`, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}` },
        body: formData,
      });
      if (!res.ok) throw new Error("Upload failed");
      return res.json();
    },

    delete: (token: string, id: string) =>
      apiFetch<void>(`/resumes/${id}`, {
        method: "DELETE",
        headers: authHeaders(token),
      }),

    update: (token: string, id: string, displayName: string) =>
      apiFetch<{ id: string; filename: string; format: string; display_name: string; created_at: string }>(
        `/resumes/${id}`,
        {
          method: "PATCH",
          headers: authHeaders(token),
          body: JSON.stringify({ display_name: displayName }),
        }
      ),
  },

  /** Tailoring */
  tailoring: {
    create: (
      token: string,
      body: {
        resume_id: string;
        job_description: string;
        action: "tailor_tex" | "tailor_docx" | "cover_letter";
      }
    ) =>
      apiFetch<{ id: string; status: string }>("/tailoring/requests", {
        method: "POST",
        headers: authHeaders(token),
        body: JSON.stringify(body),
      }),

    get: (token: string, id: string) =>
      apiFetch<{ id: string; status: string; output_id?: string }>(
        `/tailoring/requests/${id}`,
        { headers: authHeaders(token) }
      ),
  },

  /** Outputs */
  outputs: {
    get: (token: string, id: string) =>
      apiFetch<{ id: string; filename: string; format: string }>(
        `/outputs/${id}`,
        { headers: authHeaders(token) }
      ),

    downloadUrl: (id: string) => `${API_BASE_URL}/outputs/${id}/download`,
  },
};
