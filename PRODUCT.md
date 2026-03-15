# Product

## Working title
[Project Name]

## One-line summary
A production-ready application built with multiple collaborating AI agents handling planning, scaffolding, implementation, testing, bug fixing, and git/PR workflows.

## Problem statement
Describe the real problem this product solves in 3 to 6 lines.

Suggested prompts to fill this:
- Who has the problem?
- What do they do today instead?
- Why is the current solution painful, slow, expensive, or fragmented?
- Why is this product worth building now?

## Target users
### Primary users
- [User type 1]
- [User type 2]

### Secondary users
- [User type 3]

## Core jobs to be done
1. [Main workflow 1]
2. [Main workflow 2]
3. [Main workflow 3]

## Core features for v1
- [Feature 1]
- [Feature 2]
- [Feature 3]
- [Feature 4]
- [Feature 5]

## Non-goals for v1
- [Out of scope item 1]
- [Out of scope item 2]
- [Out of scope item 3]

## Product constraints
- The codebase must be production-ready.
- Agents are expected to scaffold missing project structure when needed.
- Agents should prefer simple architecture first.
- Agents should keep documentation, tests, contracts, and implementation aligned.
- Changes should be small, reviewable, and git-friendly.
- Pull request creation should be possible through local git/GitHub CLI or an external autonomous git workflow.

## Preferred default stack if unspecified
- Frontend: Next.js + TypeScript
- Backend: FastAPI + Python
- Database: PostgreSQL
- Auth: token/session-based auth
- Infra: Docker + GitHub Actions
- Testing: unit + integration + e2e
- API style: REST + OpenAPI

## Functional requirements
- The system should support user authentication if the product requires accounts.
- The system should expose a structured backend API.
- The frontend should handle loading, empty, error, and success states.
- The system should have a testable architecture and clear module boundaries.
- The system should support local development using a documented setup.

## Non-functional requirements
- Strong typing where the language supports it
- Clear validation and error handling
- Good developer ergonomics
- Stable testing strategy
- Reproducible local environment
- Easy onboarding for both humans and AI agents
- Safe configuration handling

## Success criteria for v1
- A new developer or agent can clone the repo and understand where to work.
- Backend and frontend can be implemented in parallel without constant collisions.
- Test and validation flows are established.
- Git branches and pull request workflows are clean.
- Memory files make it easy for any future agent to resume work.

## Open product questions
- [Question 1]
- [Question 2]
- [Question 3]