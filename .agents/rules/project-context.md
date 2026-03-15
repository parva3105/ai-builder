---
trigger: always_on
---

# Project Context Rule

This rule defines the default project-wide behavior that should apply to all meaningful agent work.

## Required reading order before major work
1. `PRODUCT.md`
2. `docs/primer.md`
3. `docs/memory/current-state.md`
4. `docs/memory/next-actions.md`
5. `ARCHITECTURE.md`
6. `TASKS.md`
7. `openapi.yaml` when relevant
8. `.specify/memory/constitution.md` when the task affects project-wide principles

## Project interpretation
Treat this repository as a structured multi-agent software workspace.
The repository may begin nearly empty except for rules, skills, docs, and memory.
Agents are expected to scaffold missing implementation structure when asked.

## Default expectations
- Prefer production-ready patterns over throwaway prototypes.
- Prefer simple architecture before introducing complexity.
- Keep implementation aligned with docs, contracts, and tests.
- Keep changes small, understandable, and reviewable.
- Respect likely ownership boundaries between backend, frontend, QA, and stabilization work.

## Ownership guidance
### Architect/planner
Owns:
- architecture
- service boundaries
- data model
- contracts
- milestone planning

### Backend
Owns:
- backend application structure
- routes
- services
- models
- validation
- persistence integration

### Frontend
Owns:
- application shell
- components
- route/page flows
- client-side state and API integration

### QA
Owns:
- test strategy
- CI validation
- integration/e2e coverage
- reproducible verification

### Stabilizer
Owns:
- type/lint/test failures
- small regressions
- focused cleanup related to readiness

### Git/PR operator
Owns:
- branch hygiene
- commit hygiene
- PR clarity

## Quality bar
- Strong typing where supported
- Input validation at boundaries
- Clear error handling
- No silent contract drift
- No unfinished placeholder code treated as complete
- Relevant tests for changed behavior unless the task is docs-only

## Change reporting expectation
Every meaningful task should end with:
- what changed
- files affected
- important assumptions
- risks or blockers
- the next recommended task