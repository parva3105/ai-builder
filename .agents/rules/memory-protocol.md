---
trigger: always_on
---

# Memory Protocol Rule

This rule ensures the repository remains resumable across agent iterations.

## Start-of-task protocol
Before beginning any substantial task:
1. Read `docs/primer.md`
2. Read `docs/memory/current-state.md`
3. Read `docs/memory/next-actions.md`
4. Read `docs/memory/open-questions.md` if the task touches any unresolved area
5. Read `docs/memory/decisions.md` if the task may be affected by prior durable decisions

## End-of-task protocol
Before finishing any substantial task:
1. Update `docs/memory/current-state.md`
2. Append an entry to `docs/memory/iteration-log.md`
3. Update `docs/memory/next-actions.md`
4. Update `docs/memory/decisions.md` if a durable decision changed
5. Update `docs/memory/open-questions.md` if new blockers, ambiguity, or unresolved follow-up remains

## What counts as a substantial task
A task is substantial if it changes any of the following:
- code
- contracts
- architecture
- tests
- CI
- branching/PR state
- repository structure
- milestone status

## Memory writing standards
- concise
- factual
- easy for a future agent to resume from
- no inflated language
- no duplicate long-form prose that already exists elsewhere

## Current-state writing guidance
`current-state.md` should answer:
- what exists now
- what the active stack is
- what the active branch is
- what the main blockers are
- what the last completed milestone was

## Next-actions writing guidance
`next-actions.md` should answer:
- exactly what to do next
- who should do it
- what inputs are needed
- what “done” looks like

## Iteration-log writing guidance
Each entry should record:
- role/agent
- objective
- summary
- files changed
- validation steps
- result
- next recommendation

## Non-negotiable rule
Do not finish meaningful work without updating the memory layer.