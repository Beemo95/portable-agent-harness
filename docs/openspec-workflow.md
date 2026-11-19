# Optional official OpenSpec workflows — don't reimplement them

The Markdown under `openspec/` is readable by a file-capable agent without installing OpenSpec. This template includes `openspec/config.yaml` and empty `changes/` and `specs/` folders, **not** an installed CLI, initialized upstream workflow Skills or validated game change.

## Setup in the actual project

1. Check the **current** official [installation](https://openspec.dev/docs/installation), [setup](https://openspec.dev/docs/setup), and [supported tools](https://openspec.dev/docs/supported-tools) before installing; review installed Node/OpenSpec version and the project's existing configurations.
2. In a review branch, back up/inspect existing instructions and skill folders. Run the supported `openspec init` flow with your actual tools (the CLI documents `--tools` IDs), then **review every generated diff** before committing. Do not overwrite custom Skills or approved specs.
3. Official 2.x tooling keeps canonical workflows under `.agents/skills/openspec-*/SKILL.md`. Current Antigravity, Codex, Cursor and supported Grok tools share this location; Claude Code obtains compatible links/copies under `.claude/skills/` where required. Prefer **upstream-generated** OpenSpec skills over handwritten replacements.
4. Use the official explore/propose/apply/verify/sync/archive workflow when installed. The current change's `tasks.md` remains the **single implementation checklist**, with source code and real test evidence independent from checkbox state.
5. After archiving, update STATUS to `none` or another existing active change. Keep historical decisions/knowledge in their canonical homes and topic pointers; don't leave STATUS pointing to an archived path.

## Without the CLI

Use the actual Markdown and [phase lifecycle](task-lifecycle.md) for small well-understood changes; inspect code first and report tooling/validation limits. Do **not** claim that the official OpenSpec skill commands were installed or executed. Avoid a second Python or SQLite task tracker.

References: [official setup](https://openspec.dev/docs/setup) · [supported tools](https://openspec.dev/docs/supported-tools) · [project configuration](https://openspec.dev/docs/configuration/config-yaml).
