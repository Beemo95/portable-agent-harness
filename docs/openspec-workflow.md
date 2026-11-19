# Optional official OpenSpec workflows — don't reimplement them

The Markdown under `openspec/` is readable by any file-capable agent without installing OpenSpec. The **official OpenSpec CLI and generated Skills** are optional authoring/validation helpers; they are not bundled or claimed to have been executed here.

## Setup in the actual game repository

1. Review official [OpenSpec installation](https://github.com/Fission-AI/OpenSpec#quick-start) and [supported tools](https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md). As of the referenced OpenSpec 2.x docs, npm installation uses Node.js 22.20+; confirm against current upstream before installing.
2. Install OpenSpec by your preferred **trusted** package manager (optional). In the intended project and after backing up agent configs, run `openspec init` and select only the tools you actually use. Review generated diffs before committing. Do not run forced overwrite.
3. If you change its skill profile, the current upstream documents `openspec config profile` followed by `openspec update`. Verify the actual installed version and printed instructions, not guessed slash commands.
4. Use the **upstream** skills for explore → propose → apply → update/sync → archive. New sessions can resume from the first unchecked task in the canonical change `tasks.md`. Do not use the removed custom `openspec-handoff` Skill or create a duplicate task database.
5. Keep STATUS pointing to active `openspec/changes/<slug>/` while the change is in flight. When archiving a completed change, update STATUS to `none` or the next real active change, link the archive path in history if useful, and record the actual QA status separately.

## Host differences

Official docs describe Codex's generated OpenSpec Skills under `.agents/skills/openspec-*/SKILL.md` and invoked as `$openspec-*`; Hermes uses Skills names, and Antigravity uses `.agent/skills/`. Other tools, including Grok setups, must be checked against current upstream support; don't assume automatic discovery just because a folder exists.

If the CLI is absent: edit existing OpenSpec Markdown **only when appropriate**, follow its approval process, and report the tooling limit. A checked `tasks.md` box means reported implementation, **not** independently proven gameplay or device QA.

References: [OpenSpec workflows](https://github.com/Fission-AI/OpenSpec/blob/main/docs/workflows.md) · [supported tools](https://github.com/Fission-AI/OpenSpec/blob/main/docs/supported-tools.md).
