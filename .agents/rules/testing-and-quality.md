---
trigger: model_decision
description: Apply when writing or changing code, fixing bugs, adding features, or preparing work for validation, merge, or pull request review.
---

# Testing and Quality Rule

Apply this rule when changing code, fixing bugs, adding features, or preparing work for validation, merge, or review.

## Quality principles
- Changed behavior should be validated.
- Tests should be readable and reproducible.
- Type and lint issues should be treated as part of quality work.
- Validation should be proportionate to the change.

## Minimum expectations
### Docs-only changes
- confirm the docs are internally consistent
- update memory if the change is meaningful

### Small code changes
- update or add targeted tests where relevant
- run at least the nearest practical validation

### Feature work
- add or update tests
- validate main behavior
- record any uncovered risks

## Suggested testing layers
- unit tests for focused business logic
- integration tests for service boundaries and data flows
- e2e tests for critical user journeys
- smoke checks for basic boot and health behavior

## Validation honesty rule
Never claim work is validated if it was not actually validated.
If checks were not run, say so clearly.
If checks failed, say so clearly.

## Code quality expectations
- readable naming
- cohesive modules
- explicit validation
- meaningful error handling
- no dead code from the task
- no silent contract mismatches

## Merge readiness
Work should not be packaged as review-ready if:
- behavior changed but no validation exists
- critical tests are broken without explanation
- docs/contracts are stale relative to the code