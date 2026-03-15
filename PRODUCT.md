# Product

## Working title
Mod-Your-Application

## One-line summary
An AI-powered job application platform that tailors resumes and cover letters from saved `.tex` and `.docx` files into polished, downloadable application-ready outputs.

## Problem statement
Students, early-career professionals, and active job seekers spend hours manually rewriting resumes and cover letters for every application. Existing tools are fragmented: some generate generic text, some break formatting, and most do not support real `.tex` or `.docx` resume workflows end-to-end. Users often copy-paste between ChatGPT, Overleaf, Word, and PDF converters, which is slow and error-prone. This product is worth building now because job applications are increasingly high-volume, AI-assisted, and ATS-driven, but users still need trustworthy, well-formatted, editable outputs they can actually submit.

## Target users
### Primary users
- Students applying for internships and new grad roles
- Job seekers tailoring resumes and cover letters across multiple applications

### Secondary users
- Professionals changing roles, industries, or seniority levels
- International applicants applying at high volume across regions
- Career coaches or placement teams helping applicants refine materials

## Core jobs to be done
1. Save and manage multiple master resumes in `.tex` and `.docx` formats under a user profile
2. Paste a job description and generate a tailored resume without losing formatting quality
3. Generate a tailored cover letter aligned with the job description and the user’s experience

## Core features for v1
- Secure signup, login, and profile management
- Upload, store, rename, and manage multiple `.tex` and `.docx` resumes
- Paste job description and choose an action: tailor LaTeX resume, tailor DOCX resume, or generate cover letter
- Resume tailoring engine that preserves structure and formatting as much as possible while improving relevance to the job description
- Download-ready output generation, including compiled PDF for `.tex` workflows and editable/exportable output for `.docx`

## Non-goals for v1
- Full job board integration or one-click job applications
- Real-time collaborative editing between multiple users
- Fully automated scoring, ranking, or guarantee of ATS success across all employers

## Product constraints
- The codebase must be production-ready.
- Agents are expected to scaffold missing project structure when needed.
- Agents should prefer simple architecture first.
- Agents should keep documentation, tests, contracts, and implementation aligned.
- Changes should be small, reviewable, and git-friendly.
- Pull request creation should be possible through local git/GitHub CLI or an external autonomous git workflow.
- The system must safely handle uploaded files and user-generated personal data.
- `.tex` handling must avoid unsafe compilation behavior and preserve template structure.
- `.docx` handling must operate on actual files, not only extracted plain text.
- Generated outputs should be reviewable and downloadable in user-friendly formats.

## Preferred default stack if unspecified
- Frontend: Next.js + TypeScript
- Backend: FastAPI + Python
- Database: PostgreSQL
- Auth: token/session-based auth
- Infra: Docker + GitHub Actions
- Testing: unit + integration + e2e
- API style: REST + OpenAPI

## Functional requirements
- The system should support user authentication and secure account management.
- The system should allow users to upload and manage multiple resumes in `.tex` and `.docx` formats.
- The system should expose a structured backend API for authentication, profile management, file storage, tailoring requests, and output retrieval.
- The frontend should handle loading, empty, error, and success states.
- The system should let users paste a job description and choose whether to tailor a `.tex` resume, tailor a `.docx` resume, or generate a cover letter.
- The system should preserve resume structure and formatting as much as possible during generation.
- The system should compile generated `.tex` into PDF when valid and provide helpful error feedback when compilation fails.
- The system should generate downloadable outputs with clear filenames such as `FirstName_LastName_Resume_CompanyName.pdf`.
- The system should have a testable architecture and clear module boundaries.
- The system should support local development using a documented setup.

## Non-functional requirements
- Strong typing where the language supports it
- Clear validation and error handling
- Good developer ergonomics
- Stable testing strategy
- Reproducible local environment
- Easy onboarding for both humans and AI agents
- Safe configuration handling
- Secure storage and access control for uploaded resumes and personal profile data
- Reasonable response times for generation, upload, and download workflows
- Reliable file processing and recovery behavior when generation or compilation fails

## Success criteria for v1
- A new developer or agent can clone the repo and understand where to work.
- Backend and frontend can be implemented in parallel without constant collisions.
- Test and validation flows are established.
- Git branches and pull request workflows are clean.
- Memory files make it easy for any future agent to resume work.
- A user can sign up, upload at least one `.tex` or `.docx` resume, paste a JD, generate a tailored output, and download it successfully.
- Generated documents are useful, editable, and preserve formatting well enough for real-world submission.
- Failures in generation, parsing, or compilation are surfaced clearly without corrupting user data.

## Open product questions
- Should v1 support side-by-side review and diff of original versus tailored resume?
- Should `.docx` output remain `.docx` first, or should PDF export also be required in v1?
- How much user control should exist over tailoring style, such as ATS-focused, concise, achievement-heavy, or technical-depth modes?