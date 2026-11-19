# Game art, UI, animation and asset pipeline

Use for sprites, tilesets, isometric scenes, particles, UI and animation. **Before making new assets or code**, inspect the project's actual scenes/scripts/import settings and prior art direction. If revisiting a domain, check [topic pointers](../topics.md), ADRs, source and previous experiments; verify old guidance against current implementation.

1. Record observed/approved resolution, pixel density, style/palette, camera angle, coordinate model, direction set (4/8), FPS, frame count, pivots and output format; **do not invent** unspecified values.
2. Honor explicitly requested implementation medium (code-driven/GDScript, vector, spritesheet/image). Never substitute an image for requested code or vice versa.
3. For substantial changes, plan small phases (e.g. movement baseline, animation, occlusion, interaction, integrated QA) with exact acceptance and **per-phase test/preview evidence**. Do not mark a phase complete when its required visual/runtime check is unrun.
4. Keep reusable editable assets/code, provenance, licensing constraints and import settings. Preserve previous scene/depth/coordinate conventions unless an approved design change supersedes them.
5. For isometric work, verify world-to-screen mapping, tile footprint, z-order/occlusion and collision with **moving** characters. For pixel art, inspect pixel snap, filtering, scaling, direction order, frame pivots and loop seams.
6. For UI, test representative device sizes/aspect ratios, touch areas, legibility and localization overflow where applicable. Deliver an **actual** Godot screenshot/video/GIF if produced; otherwise mark NOT RUN.
7. After validated changes, **distill reusable conventions and rejected approaches** into the existing architecture/ADR/research owner with code/test evidence, and index recurring topics via [topic map](../topics.md). Do not copy entire task logs into permanent rules.

A static preview or headless parse does not prove visual layering or Android/device behavior.
