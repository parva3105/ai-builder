# Open Questions

This file records unresolved issues, ambiguities, and blockers.

## Product questions
- Should v1 support side-by-side diff of original vs. tailored resume?
- Should `.docx` output also export to PDF in v1?
- How much user control over tailoring style (ATS, concise, achievement-heavy)?
- Should generated outputs be stored long-term or have a retention limit?
- Should users choose among multiple master resumes before each request? (likely yes, UI design TBD)

## Architecture questions
- Will background jobs be needed for long-running tailoring requests? (deferred to M4 — inline first)
- Should we implement refresh token rotation for v1? (deferred)
- Should the S3 adapter be built during v1 or deferred to v2? (deferred)

## Delivery questions
- Will PR creation be done via GitHub CLI, or through an external tool?
- Are there required hosting/deployment targets from day one?

## Resolved
- ~~What product is being built?~~ → TailorFlow (PRODUCT.md)
- ~~Is auth required in v1?~~ → Yes, JWT
- ~~Should the default stack remain Next.js + FastAPI + PostgreSQL?~~ → Yes (decisions.md)
- ~~Final domain model design?~~ → User, MasterResume, TailoringRequest, GeneratedOutput
- ~~Final endpoint list?~~ → 14 endpoints defined in openapi.yaml