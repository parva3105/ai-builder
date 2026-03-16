# Product

## Working title
TailorFlow

## One-line summary
An AI-powered job application platform that stores master `.tex` and `.docx` resumes, tailors them to job descriptions, generates matching cover letters, and returns polished, downloadable outputs.

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
4. Download application-ready outputs in formats users can edit or submit

## Primary v1 workflow
1. User signs up and logs in
2. User uploads one or more master resumes in `.tex` or `.docx`
3. User pastes a job description
4. User selects one action: tailor `.tex`, tailor `.docx`, or generate cover letter
5. System processes the request and shows progress or status
6. User reviews the result and downloads the generated output

## Core features for v1
- Secure signup, login, and profile management
- Upload, store, rename, and manage multiple `.tex` and `.docx` resumes
- Paste job description and choose an action: tailor LaTeX resume, tailor DOCX resume, or generate cover letter
- Resume tailoring engine that preserves structure and formatting as much as possible while improving relevance to the job description
- Download-ready output generation, including compiled PDF for `.tex` workflows and editable/exportable output for `.docx`
- Clear processing feedback for success, failure, and retry scenarios
- Per-user history or record of generated outputs for easy retrieval during a session

## Non-goals for v1
- Full job board integration or one-click job applications
- Real-time collaborative editing between multiple users
- Fully automated scoring, ranking, or guarantee of ATS success across all employers
- Rich in-browser document editing comparable to Overleaf or Word
- Browser-based drag-and-drop resume design tools

## Editing model for v1
Users will review generated outputs in the platform and download them, but rich in-browser editing is out of scope for v1.

## Product constraints
- The codebase must be production-ready.
- Agents are expected to scaffold missing project structure when needed.
- Agents should prefer simple architecture first.
- Agents should keep documentation, tests, contracts, and implementation aligned.
- Changes should be small, reviewable, and git-friendly.
- Pull request creation should be possible through local git/GitHub CLI or an external autonomous git workflow.
- The system must safely handle uploaded files and user-generated personal data.
- Uploaded resume files and generated outputs must be securely stored per user and isolated from other users.
- `.tex` handling must avoid unsafe compilation behavior and preserve template structure.
- `.docx` handling must operate on actual files, not only extracted plain text.
- Generated outputs should be reviewable and downloadable in user-friendly formats.
- LaTeX compilation should run in a sandboxed environment with controlled packages, timeouts, and safe error handling.

## Preferred default stack if unspecified
- Frontend: Next.js + TypeScript
- Backend: FastAPI + Python
- Database: PostgreSQL
- Auth: token/session-based auth
- File storage: object storage or secure file storage service
- Infra: Docker + GitHub Actions
- Testing: unit + integration + e2e
- API style: REST + OpenAPI

## Functional requirements
- The system should support user authentication and secure account management.
- The system should allow users to upload and manage multiple resumes in `.tex` and `.docx` formats.
- The system should expose a structured backend API for authentication, profile management, file storage, tailoring requests, generation status, and output retrieval.
- The frontend should handle loading, empty, error, and success states.
- The system should let users paste a job description and choose whether to tailor a `.tex` resume, tailor a `.docx` resume, or generate a cover letter.
- The system should preserve resume structure and formatting as much as possible during generation.
- The system should compile generated `.tex` into PDF when valid and provide helpful error feedback when compilation fails.
- The system should generate downloadable outputs with clear filenames such as `FirstName_LastName_Resume_CompanyName.pdf`.
- The system should generate downloadable cover letters in an editable and user-friendly format.
- The system should keep generated files associated with the requesting user and prevent cross-user access.
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
- Reasonable response times for upload, generation, review, and download workflows
- Reliable file processing and recovery behavior when generation, parsing, or compilation fails
- Safe isolation for LaTeX compilation and other file-processing operations
- Clear observability for failures in upload, generation, storage, and retrieval workflows

## Success criteria for v1
- A new developer or agent can clone the repo and understand where to work.
- Backend and frontend can be implemented in parallel without constant collisions.
- Test and validation flows are established.
- Git branches and pull request workflows are clean.
- Memory files make it easy for any future agent to resume work.
- A user can sign up, upload at least one `.tex` or `.docx` resume, paste a job description, generate a tailored output, and download it successfully.
- A user can generate a cover letter from the same job description and download it successfully.
- Generated documents are useful, editable, and preserve formatting well enough for real-world submission.
- Failures in generation, parsing, storage, or compilation are surfaced clearly without corrupting user data.
- The system handles file ownership and access securely across multiple users.

## Open product questions
- Should v1 support side-by-side review or diff of original versus tailored resume?
- Should `.docx` output remain `.docx` first, or should PDF export also be required in v1?
- How much user control should exist over tailoring style, such as ATS-focused, concise, achievement-heavy, or technical-depth modes?
- Should generated outputs be stored long-term, or only for a limited retention period?
- Should users be able to choose among multiple master resumes before each tailoring request?