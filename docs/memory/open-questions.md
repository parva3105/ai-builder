# Open Questions

This file records unresolved issues, ambiguities, and blockers.

## Product questions
- What exact product idea is being built?
- Which user workflow matters most for v1?
- Is auth required in v1?

## Architecture questions
- Should the default stack remain Next.js + FastAPI + PostgreSQL?
- Will background jobs be needed?
- Is a single deployable backend sufficient for v1?

## Delivery questions
- Will PR creation be local through git/GitHub CLI, or through a separate autonomous git tool?
- Are there any required hosting/deployment targets from day one?

## Blocked-until-answered
- Final domain model design
- Final endpoint list
- Final environment/runtime constraints

## Guidance
When a question is answered:
- remove or update it here
- reflect the answer in `docs/memory/decisions.md`
- update `docs/memory/current-state.md` if needed