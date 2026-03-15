---
name: bugfix-stabilizer
description: Stabilize the repository by fixing type errors, lint errors, failing tests, small regressions, and tightly scoped technical debt that directly affects reliability or merge readiness.
---

# Purpose
Use this skill after implementation waves or whenever the repo is unstable.

# Read first
- `docs/primer.md`
- `docs/memory/current-state.md`
- `docs/memory/next-actions.md`
- `.agents/rules/testing-and-quality.md`
- current validation output if available

# Primary responsibilities
- fix lint and type issues
- fix targeted failing tests
- remove small unsafe patterns
- improve merge readiness
- keep patches narrow and reviewable
- update memory after stabilization work

# Constraints
- do not perform broad rewrites
- do not introduce architecture changes without reason
- preserve expected behavior unless explicitly fixing a bug
- separate cleanup from feature expansion

# Output summary
Report:
- issues fixed
- files changed
- checks rerun
- remaining failures
- recommended next action