---
name: qa-validator
description: Validate repository quality by adding or refining test coverage, improving CI, reproducing issues, and identifying readiness gaps across the application.
---

# Purpose
Use this skill for validation, CI readiness, regression reporting, and test-layer improvement.

# Read first
- `PRODUCT.md`
- `ARCHITECTURE.md`
- `TASKS.md`
- `docs/primer.md`
- `docs/memory/current-state.md`
- `docs/memory/next-actions.md`
- `.agents/rules/testing-and-quality.md`
- `.agents/rules/test-files.md`

# Default scope
- `tests/**`
- CI-related files
- test configs
- validation docs/runbooks
- minimal production-code changes only when required to fix a confirmed issue

# Primary responsibilities
- add or refine unit/integration/e2e coverage
- create or refine CI validation steps
- reproduce issues clearly
- separate flaky failures from real regressions
- document how to validate the current repo state
- identify untested critical paths

# Constraints
- do not hide failing checks
- do not over-engineer tests beyond current product needs
- prefer deterministic and maintainable tests

# Output summary
Report:
- tests added or changed
- CI changes made
- failures found
- confirmed blockers
- recommended stabilization or implementation next step