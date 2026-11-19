# Optional official OpenSpec — scope, schema and validation

The Markdown in openspec/ remains readable by file-capable agents. This template has a project config and **no initialized official workflow Skills, active change or installed OpenSpec CLI**. A valid-looking Markdown file does not establish that a real OpenSpec installation has loaded it.

## Install into a real project only when needed

1. Verify installed OpenSpec and Node versions and official [installation](https://openspec.dev/docs/installation), [setup](https://openspec.dev/docs/setup) and [supported tools](https://openspec.dev/docs/supported-tools). The standalone installer is an option; npm-based installs require compatible Node.js.
2. **Current default installs Skills globally** under the user's home; this is **not portable** with the Git repo. In a reviewed actual game checkout, use `openspec init --scope project` and select the intended tools, or pass the documented `--tools` IDs. This makes project skills under .agents/skills/ and tool-specific links/copies where needed.
3. Inspect generated files and current OpenSpec ownership metadata before modifying or committing: preserve our 12 canonical non-OpenSpec Skills, Claude adapters, accepted specs and custom rules. Do not overwrite or claim commands that have not been run.
4. For substantial features use one change's proposal, design and tasks, with the **single** checklist. Official flows can explore → propose → apply → verify → sync/archive. Record real Godot test evidence independently of checkboxes.
5. When archiving a change, update .agent-docs/status.md to another actual active change or none and preserve reusable knowledge in its canonical spec/ADR/architecture owner.

## Validate settings before trusting them

The current OpenSpec documentation says invalid config fields may be ignored with a warning. Our shell CI checks the expected `schema: spec-driven` and basic structure only; it is **not a YAML parser or an OpenSpec validator**. When the CLI is present, use actual `openspec validate` and review its output. If unavailable, report NOT RUN, not PASS.

Official references: [setup](https://openspec.dev/docs/setup) · [config](https://openspec.dev/docs/configuration/config-yaml) · [default schema](https://openspec.dev/docs/schemas/spec-driven) · [supported tools](https://openspec.dev/docs/supported-tools).
