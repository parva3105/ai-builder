---
trigger: model_decision
description: Apply when scaffolding the project, defining services, changing architecture, editing API contracts, updating schemas, or modifying data flow.
---

# Architecture and Contracts Rule

Apply this rule when scaffolding the project, defining service boundaries, updating API behavior, changing schemas, or modifying the structure of the system.

## Architecture principles
- Start simple.
- Keep boundaries explicit.
- Prefer a modular monolith over premature microservices unless the product requires more.
- Make it easy for frontend and backend to work in parallel.
- Keep architecture legible from the repo layout.

## Contract principles
- Contracts are first-class artifacts.
- If API behavior changes, `openapi.yaml` should be updated.
- If major structure changes, `ARCHITECTURE.md` should be updated.
- If sequencing or dependencies change, `TASKS.md` should be updated.

## Required updates when architecture changes
When architecture or contracts change, update as needed:
- `ARCHITECTURE.md`
- `TASKS.md`
- `openapi.yaml`
- `docs/memory/current-state.md`
- `docs/memory/decisions.md` when the decision is durable

## Data and schema guidance
- Keep request/response schemas explicit.
- Keep entity boundaries understandable.
- Do not allow hidden schema drift between backend and frontend.
- Prefer named, documented structures over ad hoc payloads.

## Service boundary guidance
- Routes should not absorb all business logic.
- Business logic should be reusable and testable.
- Infrastructure details should not leak everywhere.
- Shared code should be intentional and minimal.

## Architecture review prompt
Before finalizing a structural change, ask:
- Does this simplify or complicate the repo?
- Does this make future agent work easier?
- Is this needed now or just theoretically useful?