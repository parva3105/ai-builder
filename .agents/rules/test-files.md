---
trigger: glob
globs: tests/**/*
---

# Test Files Rule

Apply this rule to all test files.

## Test principles
- Make tests readable.
- Make tests deterministic.
- Keep setup and teardown explicit.
- Prefer behavior-focused test names.
- Avoid unnecessary coupling to implementation details.

## Naming guidance
Test names should describe:
- what behavior is being exercised
- under what condition
- what outcome is expected

## Reliability guidance
- avoid brittle timing dependencies
- avoid unnecessary sleeps
- isolate fixtures
- clean up side effects
- keep tests runnable in repeated local and CI environments

## Coverage guidance
Prioritize:
- critical user journeys
- business logic edges
- integration boundaries
- regressions that have already occurred

## Anti-patterns
- giant monolithic test files without structure
- opaque test names
- hidden fixture dependencies
- tests that pass only in one local machine setup