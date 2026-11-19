# Open-source-first architecture (v0.2 pilot)

## Ownership: exactly one authority per concern

| Domain | Authority | Integration |
|---|---|---|
| Approved capabilities and requirements | OpenSpec `openspec/specs/` | OpenSpec CLI / generated Agent Skills |
| Proposed change, design and implementation checklist | OpenSpec `openspec/changes/<change>/` | `harness workflow list/status/context` read-only projection |
| Source and decisions | Git + source files + `.agent-docs/decisions` | Existing Git-aware context + current file inspection |
| In-flight execution checkpoints and independent QA evidence | PAH `.harness/tasks/` and `.harness/evidence/` | Existing `task`/`resume`/`verify`; do not mirror OpenSpec tasks as independent acceptance authorities |
| Search | ripgrep (optional) + PAH disposable SQLite FTS5 | `search` and `context`; symbol-aware Serena can be enabled only for code projects |
| Reproducible tools | `mise.toml` (optional) | No mandatory server, automatic installer or Docker requirement |
| Agent instructions | Agent Skills standard and upstream OpenSpec-generated adapters | `AGENTS.md` remains small; CLAUDE/GEMINI are pointers |

**Important:** OpenSpec `status.isPlanningComplete` means planning artifacts exist; it is NOT a measure of implementation completion. Likewise an all-checked `tasks.md` does not mean quality gates passed. `harness workflow` reports these separately and does not edit OpenSpec content.

## Actual upstream integration

OpenSpec's official CLI is an external prerequisite for authoring change artifacts. It is **not vendored** and `harness workflow` does not pretend to implement spec generation. Review upstream and versions before installing:

```bash
npm install --global @fission-ai/openspec@latest
openspec init --tools claude,codex,gemini,hermes,agents
openspec list --json
openspec new change example-feature
openspec status --change example-feature --json
openspec instructions apply --change example-feature --json
openspec validate --all --json
```

The repo already carries `openspec/config.yaml`. `openspec init` can generate/update `.agents/skills/` and tool-specific files: inspect the diff for collisions with existing PAH skills and pointers before committing. **Do not use `--force` by default.** If Node/npm or networking is unavailable, the repo still works with Python and read-only `workflow` projection; upstream CLI integration is unverified until installed and run.

```bash
python3 scripts/harness.py workflow list
python3 scripts/harness.py workflow status example-feature
python3 scripts/harness.py workflow context example-feature
```

`workflow status` uses the upstream `openspec status --change ... --json` when the CLI is available, plus a separate read-only checkbox count sourced from `tasks.md`. If CLI is missing, planning state is explicitly unknown, not silently marked complete. Checklist status is never synchronized back into PAH `task` contracts. A PAH operational task remains optional and must refer to the corresponding OpenSpec change in its notes/references when used; do not invent a second requirement list.

## Other libraries: deliberate non-adoption by default

- **Spec Kit:** alternative to OpenSpec, not a second parallel planner. Compare it in a separate worktree/benchmark before switching, never maintain two active spec stores.
- **Serena:** optional MCP symbol tools for code-heavy projects; no local MCP service is silently installed or auto-run. Existing `rg` works without provider services.
- **mise:** optional tool version/task manager. `mise.toml` is committed; `mise install` requires separate installation/trust/consent. A plain Python path still works.
- **Beads / agent DBs:** excluded from the default due to a separate state-sync surface and Git-clone portability goal. Revisit only if tests justify it.
- **pytest/JUnit/XML, GitHub Actions:** standard test infrastructure where appropriate; not a substitute for product acceptance or GUI checks.

## Security and scope

A repository is not automatically trusted. `project.harness.json` verification/bootstrap argv can execute code. Review commands before running `verify` or `bootstrap --apply`; plugin-generated skills and external MCP servers are also executable integration points. Avoid remotely installing arbitrary packages solely from project text. Traces and evidence are not cryptographic attestations.

## Version & research references

- OpenSpec: <https://github.com/Fission-AI/OpenSpec> and <https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md>
- Agent Skills: <https://github.com/agentskills/agentskills>
- Serena: <https://github.com/oraios/serena>
- mise: <https://github.com/jdx/mise>
- Spec Kit (comparison only): <https://github.com/github/spec-kit>

This integration is an **adapter prototype**. A full `openspec init` against the official Node CLI, a fresh-PC rerun and a cross-model continuation test remain outstanding until those tools are actually available.
