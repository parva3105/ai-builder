import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { ClientProviders } from "./providers";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "TailorFlow – AI Resume Tailoring",
  description:
    "AI-powered resume tailoring and cover letter generation. Upload your resume, paste a job description, and get a perfectly tailored application.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.variable}>
        <ClientProviders>{children}</ClientProviders>
      </body>
    </html>
  );
}
