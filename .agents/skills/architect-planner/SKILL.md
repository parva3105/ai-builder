---
name: architect-planner
description: Plan and refine the system architecture, service boundaries, data model, API contracts, milestone breakdown, and durable technical decisions for the project.
---

# Purpose
Use this skill for architecture, planning, and contract work before or during implementation.

# Read first
- `PRODUCT.md`
- `ARCHITECTURE.md`
- `TASKS.md`
- `docs/primer.md`
- `docs/memory/current-state.md`
- `docs/memory/next-actions.md`
- `docs/memory/decisions.md`
- `.specify/memory/constitution.md`
- `.agents/rules/project-context.md`
- `.agents/rules/architecture-and-contracts.md`

# Primary responsibilities
- refine or define system boundaries
- choose or confirm the baseline stack
- define important entities and relationships
- define auth/session approach if needed
- define backend/frontend interaction patterns
- create or update `openapi.yaml`
- expand milestone planning in `TASKS.md`
- record durable choices in `docs/memory/decisions.md`

# Deliverables
- updated `ARCHITECTURE.md`
- updated `TASKS.md`
- updated `openapi.yaml` if API work is relevant
- clearer current state and next actions
- explicit architectural assumptions

# Constraints
- prefer the simplest architecture that meets product needs
- avoid premature distributed complexity
- no deep feature implementation unless explicitly requested
- keep architecture legible and implementation-friendly

# When done
A backend agent and a frontend agent should be able to continue with minimal ambiguity.