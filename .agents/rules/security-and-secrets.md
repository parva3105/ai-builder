---
trigger: model_decision
description: Apply when working with auth, secrets, environment variables, external APIs, databases, file uploads, user data, or deployment config.
---

# Security and Secrets Rule

Apply this rule when working with auth, environment variables, secrets, external integrations, databases, file uploads, or user data.

## Core security rules
- Never hardcode secrets.
- Use environment variables for sensitive configuration.
- Never commit real credentials.
- Validate inputs at trust boundaries.
- Avoid leaking internal errors to end users.
- Prefer safe defaults and explicit checks.

## Auth guidance
If auth is present:
- keep permission boundaries explicit
- protect sensitive endpoints
- avoid assuming the client is trusted
- document the chosen auth/session flow

## External API guidance
- keep keys/config in environment variables
- handle rate limits and error responses safely
- log failures without exposing secrets
- document required external configuration

## Database guidance
- do not expose raw database credentials in code
- keep connection config externalized
- validate data at application boundaries
- avoid dangerous defaults

## File and upload guidance
- validate file types and sizes where applicable
- avoid trusting user-provided metadata blindly
- document storage/security assumptions

## Documentation obligation
When a security-sensitive choice is made, update:
- `docs/memory/decisions.md` if durable
- `.env.example` if new env variables are required
- relevant docs/contracts if behavior changes