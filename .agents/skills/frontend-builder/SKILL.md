---
name: frontend-builder
description: Build or extend the frontend foundation and features, including scaffolding, routes/screens, components, hooks, API integration, UX states, and frontend-oriented tests.
---

# Purpose
Use this skill for frontend implementation work.

# Read first
- `PRODUCT.md`
- `ARCHITECTURE.md`
- `TASKS.md`
- `docs/primer.md`
- `docs/memory/current-state.md`
- `docs/memory/next-actions.md`
- `openapi.yaml` when relevant
- `.agents/rules/project-context.md`
- `.agents/rules/frontend-react.md`
- `.agents/rules/testing-and-quality.md`

# Default scope
- `apps/web/**`
- `packages/ui/**` if present
- frontend-safe shared contracts or helpers
- frontend test files when relevant

# Primary responsibilities
- scaffold frontend structure if missing
- implement app shell and routes/screens
- implement reusable components
- implement hooks and helpers
- integrate documented backend APIs or safe mocks
- handle loading, error, empty, and success states
- add or update frontend tests where relevant

# Constraints
- do not modify backend implementation unnecessarily
- follow documented contracts
- avoid giant page components
- keep reusable UI patterns clean and composable

# Output summary
Report:
- screens/components/hooks added or changed
- API integrations added or changed
- validation/tests run
- blocked dependencies from backend or product ambiguity
- next recommended frontend or QA task