---
name: git-pr-operator
description: Prepare clean branches, focused commits, and review-ready pull request artifacts using available git tooling, or generate a complete PR draft when direct PR tooling is unavailable.
---

# Purpose
Use this skill when work needs to be committed, packaged, or proposed for review.

# Read first
- `docs/memory/current-state.md`
- `docs/memory/next-actions.md`
- `.agents/rules/workflow-and-branching.md`
- current git diff/status if available
- current validation status if available

# Primary responsibilities
- confirm or create an appropriate task branch
- review changed files for scope
- prepare focused commits
- generate or create a PR when requested
- report validation status honestly
- keep branch/PR state reflected in memory files if material

# If tooling is available
Use:
- `git` for branching, staging, commits
- `gh` for PR creation when available

# If direct PR tooling is not available
Generate:
- recommended branch name
- commit plan
- PR title
- PR body
- reviewer checklist
- validation notes

# Constraints
- do not hide failing checks
- keep PR scope focused
- do not package unrelated concerns together
- make reviewer instructions explicit

# Output summary
Report:
- branch used or recommended
- commits created or proposed
- PR created or drafted
- validation status
- follow-up actions for reviewer or next agent