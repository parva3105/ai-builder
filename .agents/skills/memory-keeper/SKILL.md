---
name: memory-keeper
description: Update the project memory layer so future agent iterations can resume quickly with an accurate current state, clear next action, and durable decision trail.
---

# Purpose
Use this skill at the end of major work or whenever the repo state has materially changed.

# Read first
- `docs/primer.md`
- `docs/memory/current-state.md`
- `docs/memory/iteration-log.md`
- `docs/memory/next-actions.md`
- `docs/memory/decisions.md`
- `docs/memory/open-questions.md`
- `.agents/rules/memory-protocol.md`

# Required outputs
Update:
- `docs/memory/current-state.md`
- `docs/memory/iteration-log.md`
- `docs/memory/next-actions.md`

Conditionally update:
- `docs/memory/decisions.md`
- `docs/memory/open-questions.md`

# Responsibilities
- capture the new repo truth
- record exactly what changed
- make the next resume point obvious
- keep entries concise and factual
- remove stale state where needed

# Writing rules
- concise
- factual
- no fluff
- no inflated claims
- no hidden blockers

# Completion standard
A future agent should be able to open the repo, read the memory files, and continue without rereading the entire history.