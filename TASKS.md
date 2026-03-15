# Tasks

This file is the primary milestone and execution tracker for both humans and AI agents.

## Working rules
- Keep tasks concrete and implementation-friendly.
- Prefer vertical slices where possible.
- Update this file whenever major work is completed, blocked, or reprioritized.
- Keep this aligned with the memory layer.

---

## M0 - Foundations and planning
- [ ] Finalize product framing in `PRODUCT.md`
- [ ] Expand `ARCHITECTURE.md`
- [ ] Confirm default stack or choose a different stack
- [ ] Scaffold initial repo structure
- [ ] Create starter backend layout
- [ ] Create starter frontend layout
- [ ] Create starter testing layout
- [ ] Create local environment baseline
- [ ] Create initial CI baseline
- [ ] Create initial `openapi.yaml`
- [ ] Update memory files after bootstrap

## Exit criteria
- Project structure exists
- Docs are readable
- Repo is ready for backend and frontend parallel work

---

## M1 - Backend foundation
- [ ] Create backend app entry point
- [ ] Create config management
- [ ] Create health endpoint
- [ ] Create auth baseline if needed
- [ ] Create database connection layer
- [ ] Create initial schemas/models
- [ ] Create first service modules
- [ ] Create initial integration tests
- [ ] Update API contract

## Exit criteria
- Backend boots locally
- Health check works
- Core backend structure is stable
- Contract is documented

---

## M2 - Frontend foundation
- [ ] Create frontend app shell
- [ ] Create routing/layout
- [ ] Create global styling baseline
- [ ] Create reusable component structure
- [ ] Create API client layer
- [ ] Create first feature flow
- [ ] Create frontend tests
- [ ] Handle loading/error/empty states

## Exit criteria
- Frontend boots locally
- A user can navigate a basic app shell
- Frontend can call backend or use mock data safely

---

## M3 - Core product implementation
- [ ] Implement primary user journey 1
- [ ] Implement primary user journey 2
- [ ] Implement supporting backend logic
- [ ] Implement persistence for core domain entities
- [ ] Implement validation and business rules
- [ ] Expand tests for core product paths
- [ ] Update docs and memory

## Exit criteria
- Core workflows are usable end-to-end
- Tests cover main behavior
- Contracts and implementation are aligned

---

## M4 - Validation and stabilization
- [ ] Tighten lint/type checks
- [ ] Fix failing tests
- [ ] Add e2e coverage
- [ ] Improve logs and errors
- [ ] Improve developer docs
- [ ] Resolve major blockers
- [ ] Review security-sensitive areas
- [ ] Prepare PR-ready changes

## Exit criteria
- Repo is stable
- Validation is reproducible
- Main blockers are removed or documented

---

## M5 - Release readiness
- [ ] Confirm local setup steps
- [ ] Confirm build steps
- [ ] Confirm environment variables
- [ ] Confirm deployment assumptions
- [ ] Confirm smoke test
- [ ] Create release checklist
- [ ] Finalize next-stage backlog

## Exit criteria
- A reviewer can understand how to run and validate the project
- Release steps are documented

---

## Current priority
- [ ] Fill this in after the first planning run

## Known blockers
- [ ] Fill this in after the first planning run

## Backlog
- [ ] Add ADR process if architecture becomes complex
- [ ] Add observability dashboards if scale requires it
- [ ] Add worker/background job layer if the product requires async processing