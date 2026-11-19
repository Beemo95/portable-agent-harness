---
name: project-bootstrap
description: Reproduce a repository on a fresh machine without inventing dependencies or resetting prior work.
---
# Project bootstrap (cold entry / brownfield)

Use on first entry to a repository, new machine, or new domain. Never overwrite existing project intent or test baselines.

1. Read repository `AGENTS.md` and `.agent-docs/INDEX.md`; inspect actual root layout.
2. Run `python3 scripts/harness.py doctor` and `python3 scripts/harness.py lint`.
3. Review `project.harness.json`; preview `bootstrap` commands, request approval before executing unfamiliar install/modify actions.
4. Enumerate actual source-of-truth documents and available test commands; identify credentials or assets that are external blockers without exposing them.
5. Run the preexisting smoke tests on unchanged code and record the baseline separately from feature QA.
6. Record verified architecture paths and context route hints; keep docs short and evidence-linked.
7. For an existing project, prefer minimal adaptation; do not rebuild architecture or rewrite old test fixtures to match new code.

Output: usable environment or explicit blocker report, verified project map, known baseline, next steps.
