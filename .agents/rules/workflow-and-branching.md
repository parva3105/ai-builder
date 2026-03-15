---
trigger: model_decision
description: Apply when the task involves planning, multi-step execution, git branches, commits, pull requests, multiple agents, or handoffs between agents.
---

# Workflow and Branching Rule

Apply this rule when planning, coordinating multiple steps, using git branches, packaging work for review, or handing work across agent boundaries.

## Workflow principles
- Plan before deep implementation.
- Break large work into small slices.
- Prefer one branch per major task.
- Prefer one concern per PR.
- Keep the next reviewer’s job easy.

## Recommended branch naming
- `agent/bootstrap/<task>`
- `agent/arch/<task>`
- `agent/backend/<task>`
- `agent/frontend/<task>`
- `agent/qa/<task>`
- `agent/fix/<task>`
- `agent/pr/<task>`

## Commit guidance
- Use focused commits.
- Write descriptive commit messages.
- Do not batch unrelated concerns together.
- Keep refactors separate from behavior changes when possible.

## Handoff guidance
When a task ends and another role should continue:
- update `docs/memory/next-actions.md`
- record blockers and assumptions
- make the handoff explicit
- avoid leaving ambiguous partially-done state

## Pull request readiness checklist
Before opening or proposing a PR:
- review changed files
- confirm the branch is scoped correctly
- run relevant checks where possible
- summarize behavior changes
- summarize how to validate
- list known limitations or failing checks honestly

## Tool behavior
If git and GitHub CLI are available:
- create a scoped branch if needed
- stage only relevant files
- create focused commits
- create or update a PR when asked

If direct PR tooling is not available:
- prepare:
  - branch name
  - commit plan
  - PR title
  - PR body
  - reviewer checklist

## Anti-patterns
- mixing planning, refactor, features, and fixes in one PR
- vague commit messages
- hiding failing validation
- leaving no clear next owner