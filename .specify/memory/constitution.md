# Constitution

This file defines the enduring operating constitution for the repository.
It should remain stable and should only change when the project’s governance or engineering philosophy changes materially.

## Mission
Build a production-ready software product using a multi-agent development workflow that is structured, reviewable, testable, and easy to resume across iterations.

## Core constitutional principles

### 1. Clarity over cleverness
The codebase, docs, contracts, and workflows should be easy for both humans and agents to understand.
Avoid opaque abstractions unless clearly justified.

### 2. Contracts are first-class
Architecture, APIs, and schemas are not side notes.
When behavior changes, the relevant contracts and docs should be updated.

### 3. Memory must remain usable
The project must be resumable from its documented memory layer.
No major iteration is complete unless the state and next steps are recorded.

### 4. Small, reviewable changes
Prefer narrow, well-scoped branches and commits over large, mixed changes.
A reviewer should be able to understand what changed and why.

### 5. Quality is part of delivery
Testing, validation, and error handling are part of implementation, not separate afterthoughts.

### 6. Security by default
Secrets must not be hardcoded.
Input validation, safe configuration, and least-privilege thinking should be standard behavior.

### 7. Simplicity before scale
Start with the simplest architecture that can support the product goals.
Do not introduce distributed complexity before it is justified.

### 8. Explicit ownership
Each major workstream should have a clear owner:
- architecture/planning
- backend
- frontend
- QA/validation
- bugfix/stability
- git/PR packaging

### 9. Honest status reporting
Agents should not hide uncertainty, failing checks, or blockers.
Status should be factual and easy to audit.

### 10. Reversibility matters
Prefer decisions that are easy to revise early in the project.
Lock in complexity only when necessary.

## Constitutional workflow obligations
For major work:
- read the product and memory context first
- keep tasks scoped
- update the memory layer before stopping
- keep docs/contracts aligned with implementation
- preserve a clear next action for future work

## Definition of a constitution-level change
A change belongs in this file only if it changes:
- project-wide development philosophy
- review standards
- security posture
- quality bar
- ownership model
- architectural governance

Routine progress should never be recorded here.