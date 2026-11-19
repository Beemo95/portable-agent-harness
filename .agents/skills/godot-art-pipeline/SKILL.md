---
name: godot-art-pipeline
description: Plan, produce or integrate Godot game art, pixel sprites, directional animation, isometric tilemaps, UI or VFX. Use when art sources, import settings or visible previews matter.
---

# Godot art pipeline

1. Read `ai-docs/rules/design-art.md` and relevant existing art/reference scenes. Identify expected output format (GDScript-generated/vector/image); don't substitute one for another.
2. Document actual target size, frames/directions, camera/projection, palette and pivots from approved spec, not guesses.
3. Build/edit reusable source assets or code, keep provenance and import settings, then integrate into a real Godot scene when asked.
4. Test filtering/pixel snap, direction ordering, collisions, depth ordering, screen sizes and animation loops as appropriate.
5. Deliver editable files, exact scene paths, actual rendered preview where available and a clear NOT RUN note when Godot was unavailable.

For pixel/isometric work, load [pixel-isometric checklist](references/pixel-isometric-checklist.md) only when relevant.
