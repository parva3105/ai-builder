---
trigger: glob
globs: apps/web/**/*.{ts,tsx,js,jsx}
---

# Frontend React Rule

Apply this rule to frontend React and TypeScript files.

## Frontend structure guidance
- Keep components small and composable.
- Separate presentation from heavy logic where practical.
- Centralize API access and data-fetching helpers.
- Handle loading, empty, success, and error states explicitly.
- Prefer accessibility-aware markup and interactions.

## Suggested layout
- `app/` or route layer for pages/screens
- `components/` for reusable UI pieces
- `features/` for domain-oriented modules
- `hooks/` for reusable behavior
- `lib/` for API clients and platform helpers
- `types/` for frontend-safe types
- `tests/` for UI and behavior checks where applicable

## State management guidance
- start with the simplest state model that works
- avoid global complexity before it is needed
- keep state ownership clear

## UI quality guidance
- avoid giant page components
- keep props meaningful
- avoid duplicated UI logic when a reusable abstraction is justified
- ensure important error states are not ignored

## Contract guidance
Frontend should follow documented API contracts.
If the frontend must assume a payload shape, that assumption should be traceable to `openapi.yaml` or another explicit shared contract.