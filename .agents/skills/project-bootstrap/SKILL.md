---
name: project-bootstrap
description: Bootstrap a brand-new repository by creating scaffolding, starter folders, initial docs, environment templates, CI baseline, and a clean foundation for parallel agent work.
---

# Purpose
Use this skill when the repository is new, mostly empty, or missing the actual application structure.

# Read first
- `PRODUCT.md`
- `ARCHITECTURE.md`
- `TASKS.md`
- `docs/primer.md`
- `docs/memory/current-state.md`
- `docs/memory/next-actions.md`
- `.agents/rules/project-context.md`
- `.agents/rules/memory-protocol.md`
- `.agents/rules/architecture-and-contracts.md`

# Primary objectives
- create the initial application folder structure
- scaffold backend and frontend foundations if the stack is clear
- create test folders
- create CI baseline
- create docker baseline if relevant
- create `.env.example` if missing
- create or refine `openapi.yaml`
- update architecture and task tracking to reflect the scaffold
- update the memory layer

# Expected deliverables
Depending on the product and chosen stack, this may include:
- `apps/web/`
- `apps/api/`
- `tests/`
- `.github/workflows/`
- `docker-compose.yml`
- `.env.example`
- starter configs and package/runtime files
- `docs/runbooks/local-setup.md`

# Constraints
- do not implement deep product-specific business logic unless explicitly asked
- prefer minimal scalable scaffolding
- make assumptions explicit
- do not invent major product requirements
- keep the repo easy for specialized agents to continue from

# Working style
- create the smallest useful scaffold
- document what was created
- note which assumptions should be confirmed by the user
- update memory files before finishing

# Output summary format
At the end, summarize:
- folders/files created
- stack assumptions used
- unresolved decisions
- exact recommended next task