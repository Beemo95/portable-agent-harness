---
name: godot-art-pipeline
description: Implement or integrate Godot pixel/isometric art, directional animation, tilemaps and UI with real previews and reusable decisions.
---
# Godot art pipeline

1. Inspect existing art/scene code, assets, import settings and [prior topic knowledge](../../../.agent-docs/topics.md) before generating a new design. Verify past facts against current source.
2. Read [art/design rule](../../../.agent-docs/rules/design-art.md). Determine **requested output format** from user intent (GDScript/code, editable vector, image/sprites) and never swap media silently.
3. Record existing or approved direction count, camera/isometric projection, pixel density, dimensions, palette, pivots, frame count and FPS; do not guess from unavailable assets.
4. For significant work, plan testable phases with required visual/runtime evidence. Integrate and check moving-character z-order, animation transitions, pixel snapping, import and collisions as relevant.
5. Do not mark a phase visually verified without actually running/inspecting the scene. Report NOT RUN if unavailable; capture actual editable resources and screenshot/video/GIF where possible.
6. After confirmed progress, distill reusable coordinate/animation/depth rules or proven failure causes into canonical architecture/ADR/research with code/test links; add topic pointers for future related work.

Only read [pixel/isometric checklist](references/pixel-isometric-checklist.md) when relevant.
