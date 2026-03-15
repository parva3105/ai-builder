# Primer

This file is the durable project reference for future agent iterations.
It should stay high-signal, stable, and mostly free of temporary noise.

## Project identity
This repository is a multi-agent software workspace designed so that planning, scaffolding, implementation, testing, bug fixing, and git/PR preparation can happen cleanly and incrementally.

## Core operating principles
- Prefer simple architecture first.
- Prefer small, reviewable changes.
- Keep contracts and implementation synchronized.
- Keep tests aligned with changed behavior.
- Keep memory files current so any future agent can resume efficiently.
- Avoid broad rewrites unless explicitly requested.

## Source of truth reading order
Agents should read these in order before major work:
1. `PRODUCT.md`
2. `docs/primer.md`
3. `docs/memory/current-state.md`
4. `docs/memory/next-actions.md`
5. `ARCHITECTURE.md`
6. `TASKS.md`
7. `openapi.yaml` if present and relevant

## Default repository conventions
### Frontend
- small, modular components
- reusable hooks/utilities
- clear UX state handling
- centralized API access

### Backend
- thin routes
- business logic in services
- explicit schemas/models
- validation at boundaries
- configuration separated from business logic

### Testing
- unit tests for logic
- integration tests for boundaries
- e2e tests for critical user flows
- avoid brittle/flaky test patterns

### Git
- one branch per major task
- focused commits
- no vague PRs
- do not hide failing checks

## Expected collaboration model
- Architect plans and defines contracts first
- Backend and frontend can then work in parallel
- QA validates behavior and CI flows
- Stabilizer fixes regressions and readiness issues
- Git/PR operator packages changes cleanly

## Memory policy
This project relies on the memory layer to make future iterations efficient.
At the end of meaningful work, agents should update:
- current state
- iteration log
- next actions
- decisions when durable choices changed
- open questions when uncertainty or blockers remain

## Definition of done for a meaningful task
A task is not fully done unless:
- the main objective was completed or explicitly blocked
- affected docs/contracts were updated if needed
- relevant tests were added or updated where appropriate
- memory files reflect the new truth
- the next resume point is clear

## Anti-patterns to avoid
- giant ambiguous commits
- undocumented contract changes
- duplicate logic across backend/frontend without reason
- placeholder production code marked as “done”
- changing too many areas at once without explanation
- leaving the next step unclear

## How to evolve this file
Only put durable information here.
Do not turn this into a noisy daily log.
Use the memory files for iteration-specific state.