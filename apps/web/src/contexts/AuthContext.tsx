"use client";

import {
  createContext,
  useContext,
  useState,
  useEffect,
  useCallback,
  type ReactNode,
} from "react";
import { api } from "@/lib/api";
import type { UserProfile } from "@/types/api";

// ── Types ────────────────────────────────────────────────────

interface AuthState {
  user: UserProfile | null;
  accessToken: string | null;
  refreshToken: string | null;
  isLoading: boolean;
  isAuthenticated: boolean;
}

interface AuthContextValue extends AuthState {
  login: (email: string, password: string) => Promise<void>;
  signup: (
    email: string,
    password: string,
    fullName: string
  ) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextValue | null>(null);

// ── Storage helpers ──────────────────────────────────────────

const STORAGE_KEYS = {
  accessToken: "tf_access_token",
  refreshToken: "tf_refresh_token",
} as const;

function getStoredToken(key: string): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem(key);
}

function storeTokens(accessToken: string, refreshToken: string) {
  localStorage.setItem(STORAGE_KEYS.accessToken, accessToken);
  localStorage.setItem(STORAGE_KEYS.refreshToken, refreshToken);
}

function clearTokens() {
  localStorage.removeItem(STORAGE_KEYS.accessToken);
  localStorage.removeItem(STORAGE_KEYS.refreshToken);
}

// ── Hydration helper ─────────────────────────────────────────

async function hydrateUser(
  access: string,
  refresh: string
): Promise<{
  user: UserProfile;
  accessToken: string;
  refreshToken: string;
}> {
  try {
    const profile = await api.auth.me(access);
    return {
      user: profile as UserProfile,
      accessToken: access,
      refreshToken: refresh,
    };
  } catch {
    // Access token expired – try refresh
    const res = await api.auth.refresh(refresh);
    const newAccess = res.access_token;
    storeTokens(newAccess, refresh);
    const profile = await api.auth.me(newAccess);
    return {
      user: profile as UserProfile,
      accessToken: newAccess,
      refreshToken: refresh,
    };
  }
}

// ── Hydration promise (singleton, runs once on module load in browser) ──

let hydrationPromise: Promise<{
  user: UserProfile;
  accessToken: string;
  refreshToken: string;
} | null> | undefined;

function getHydrationPromise() {
  if (hydrationPromise !== undefined) return hydrationPromise;

  const access = getStoredToken(STORAGE_KEYS.accessToken);
  const refresh = getStoredToken(STORAGE_KEYS.refreshToken);

  if (!access || !refresh) {
    hydrationPromise = Promise.resolve(null);
    return hydrationPromise;
  }

  hydrationPromise = hydrateUser(access, refresh).catch(() => {
    clearTokens();
    return null;
  });

  return hydrationPromise;
}

// ── Provider ─────────────────────────────────────────────────

export function AuthProvider({ children }: { children: ReactNode }) {
  const [accessToken, setAccessToken] = useState<string | null>(() =>
    getStoredToken(STORAGE_KEYS.accessToken)
  );
  const [refreshToken, setRefreshToken] = useState<string | null>(() =>
    getStoredToken(STORAGE_KEYS.refreshToken)
  );
  const [user, setUser] = useState<UserProfile | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  // Resolve the singleton hydration promise inside a useEffect
  // This avoids setting state during the initial render phase before the component mounts
  useEffect(() => {
    let mounted = true;

    if (isLoading) {
      const promise = getHydrationPromise();
      promise.then((result) => {
        if (!mounted) return;
        
        if (result) {
          setUser(result.user);
          setAccessToken(result.accessToken);
          setRefreshToken(result.refreshToken);
        } else {
          setAccessToken(null);
          setRefreshToken(null);
          setUser(null);
        }
        setIsLoading(false);
      });
    }

    return () => {
      mounted = false;
    };
  }, [isLoading]);

  const login = useCallback(async (email: string, password: string) => {
    const res = await api.auth.login(email, password);
    setAccessToken(res.access_token);
    setRefreshToken(res.refresh_token);
    storeTokens(res.access_token, res.refresh_token);

    const profile = await api.auth.me(res.access_token);
    setUser(profile as UserProfile);
  }, []);

  const signup = useCallback(
    async (email: string, password: string, fullName: string) => {
      const res = await api.auth.register(email, password, fullName);
      setAccessToken(res.access_token);
      setRefreshToken(res.refresh_token);
      storeTokens(res.access_token, res.refresh_token);

      const profile = await api.auth.me(res.access_token);
      setUser(profile as UserProfile);
    },
    []
  );

  const logout = useCallback(() => {
    setUser(null);
    setAccessToken(null);
    setRefreshToken(null);
    clearTokens();
    // Reset hydration so next mount re-checks
    hydrationPromise = undefined;
  }, []);

  const value: AuthContextValue = {
    user,
    accessToken,
    refreshToken,
    isLoading,
    isAuthenticated: !!user && !!accessToken,
    login,
    signup,
    logout,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

// ── Hook ─────────────────────────────────────────────────────

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return ctx;
}
