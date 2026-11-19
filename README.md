# Portable Agent Harness — code-first, Git-native, Godot-oriented

A small **Markdown + Git + OpenSpec** profile for AI-assisted development. When asked to build a feature, the agent should investigate existing code and prior decisions, ask only truly unresolved user questions, plan testable phases, implement and verify them in order, then preserve reusable discoveries for future separate tasks. No mandatory Python/SQLite, task database, MCP server or context-packet engine.

> **This repository is a template, not a playable game.** It contains no inspected Godot game code. Use [safe adoption](docs/adopting-existing-project.md) to merge these rules into a real project.

## Two complementary workflows

**Development:** code + existing tests + relevant knowledge → clarify blocking choices → OpenSpec proposal/design + phased `tasks.md` → one implementation slice + automated tests → real verification gate → next phase (or block) → durable distillation.

**Months-later reuse:** new isometric feature → inspect current scene/code → look up [topic pointers](.agent-docs/topics.md), ADRs, archived changes and actual tests → reconcile old conventions → reuse proven work without rediscovering it.

| Kind of record | Canonical owner |
| --- | --- |
| Short agent instructions and routing | [AGENTS.md](AGENTS.md) |
| Current work, verified/untested, next action | [STATUS](.agent-docs/status.md) |
| Product/feature acceptance and phases | `openspec/specs/` and `openspec/changes/` |
| Reusable domain discovery | [Topic map](.agent-docs/topics.md), **pointers only** |
| Verified architecture / why decisions were made | [Architecture](.agent-docs/architecture.md) / [ADRs](.agent-docs/decisions/) |
| Durable external research / meaningful handoff | [Research](.agent-docs/research/) / [worklogs](.agent-docs/worklog/) |
| Code, regression and real QA evidence | Actual source/test files, command results, device/runtime artifacts |

## Key documents
[Phase lifecycle](docs/task-lifecycle.md) · [Knowledge distillation/retrieval](docs/knowledge-reuse.md) · [Selective context](docs/context-engineering.md) · [Official OpenSpec workflow](docs/openspec-workflow.md) · [Godot adoption](docs/godot-profile.md) · [Agent compatibility limits](docs/agent-adapters.md) · [Evaluation](docs/evaluation.md)

## Documentation-only checks
```sh
bash scripts/check-docs.sh
bash tests/docs-lint.sh
```

GitHub Actions runs structural Markdown/STATUS checks; scripts/tests are allowed for real projects. **These checks do not run Godot, enforce model behavior or demonstrate cross-model recall.** You must use actual game tests and the [evaluation scenarios](docs/evaluation.md) to measure the above workflows.

OpenSpec's official CLI/Skills are optional upstream authoring tools; Markdown remains readable without installation. Agents must check real code and tests rather than treating old text or success reports as proof. Git only transfers committed/pushed non-secret state. Older branches may contain the deprecated Python design; inspect before reusing.

MIT license: [LICENSE](LICENSE).
