    # TailorFlow

This repository is designed to be developed by multiple AI agents and human reviewers working together in a structured, git-friendly workflow.

## Repository purpose
See `PRODUCT.md` for the product definition and goals.

## Repository operating model
This repo uses:
- `.agents/rules/` for always-on, model-decision, and file-targeted behavioral rules
- `.agents/skills/` for specialized agent workflows
- `docs/primer.md` for durable project guidance
- `docs/memory/` for resume-friendly repo memory across iterations

## Philosophy
- Keep the repo understandable
- Prefer simple architecture first
- Let agents scaffold missing structure when needed
- Keep code, docs, contracts, and tests aligned
- Favor small, reviewable changes

## Recommended default stack
If not explicitly overridden in `PRODUCT.md`:
- Frontend: Next.js + TypeScript
- Backend: FastAPI + Python
- Database: PostgreSQL
- API: REST + OpenAPI
- Testing: unit, integration, and e2e
- Infra: Docker + GitHub Actions

## Agent roles
### Architect
Owns:
- planning
- architecture
- service boundaries
- API contracts
- durable decisions

### Backend
Owns:
- backend structure
- routes
- services
- models
- validation
- backend tests

### Frontend
Owns:
- frontend structure
- components
- pages
- API integration
- UX state handling

### QA
Owns:
- validation strategy
- integration and e2e coverage
- CI checks
- reproducible verification

### Bugfix/Stabilizer
Owns:
- lint issues
- type issues
- flaky tests
- focused regressions
- cleanup directly related to stability

### Git/PR operator
Owns:
- branch hygiene
- focused commits
- PR drafting/creation
- clear validation notes

## Memory workflow
Before major work, agents should read:
1. `PRODUCT.md`
2. `docs/primer.md`
3. `docs/memory/current-state.md`
4. `docs/memory/next-actions.md`

After major work, agents should update:
1. `docs/memory/current-state.md`
2. `docs/memory/iteration-log.md`
3. `docs/memory/next-actions.md`
4. `docs/memory/decisions.md` when durable choices change
5. `docs/memory/open-questions.md` when new blockers or uncertainty appear

## Suggested startup sequence
1. Initialize git and connect GitHub
2. Commit the control layer
3. Run the first planning/bootstrap prompt
4. Review scaffold and plan
5. Run backend and frontend work in parallel
6. Run QA
7. Run stabilization and PR preparation

## First prompt recommendation
Start with a planning/bootstrap run that:
- reads the product and memory files
- scaffolds the repo
- expands architecture
- expands tasks
- prepares initial contracts
- updates memory files

## Notes
This README is intentionally operational. Product-specific usage and run commands should be added once the actual app structure exists.