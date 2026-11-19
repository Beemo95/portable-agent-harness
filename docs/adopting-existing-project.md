# Adoption without overriding existing work

There is **no installer**. Make a branch, inspect the existing game's AGENTS/agent configs, specs, tests and source. Copy/merge only useful documentation: `AGENTS.md`, `.agent-docs/`, `.agents/skills/`, optional provider pointers and `openspec/`. Do **not** overwrite approved rules or existing tests.

Replace template placeholders in `product.md`, `architecture.md` and `status.md` with **observed facts**: Godot version/renderer/platform, core scenes, current work, acceptance, evidence, blockers and next action. Keep one canonical OpenSpec tasks checklist; link existing issues/PRs if present.

Test the baseline in the real project and a cold new-session/clean-clone recovery before relying on handoffs. Commit/push non-secret context/source. If migrating an old PAH installation, inspect dependencies before removing its scripts or `.harness/` files.

Godot headless checks alone don't prove scenes visually correct.
