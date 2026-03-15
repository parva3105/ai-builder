# Next Actions

This file should tell the next agent exactly where to resume.

## Immediate next task
- Initialize git, connect GitHub remote, and commit the control layer
- Run the first planning/bootstrap iteration
- Scaffold the app structure and update architecture/tasks accordingly

## Recommended owner
- project-bootstrap
- architect-planner
- memory-keeper

## Required inputs
- completed `PRODUCT.md`
- current repo structure
- desired default stack confirmation if different from the baseline

## Definition of done for the next task
- repo is initialized and connected to GitHub
- first planning/bootstrap run has completed
- application folder structure exists
- memory files reflect the new state

## Follow-up after that
- backend foundation pass
- frontend foundation pass
- QA validation pass
- bugfix/stabilization pass
- git/PR packaging pass

## Notes for the next agent
- Do not jump straight into deep feature implementation on the first run.
- Scaffold and plan first.
- Keep assumptions explicit.