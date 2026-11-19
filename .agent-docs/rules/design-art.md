# Game art, UI, animation and asset pipeline

Read when producing or integrating sprites, tilesets, isometric scenes, particles, UI or animation. Read project art direction and reference assets before producing new work.

1. Record target resolution, pixel density, style, palette, camera angle, coordinate system, direction set (4/8), FPS, frame count and export requirements **only as specified or observed**; don't guess.
2. Decide the implementation format from the requested outcome: code-driven geometry/GDScript, reusable vector resources, or image sprites. Do **not** silently replace a requested code-based asset with an image or vice versa.
3. Preserve source files and editability (e.g., scripts/shaders/source sprite sheets). Track license, origin and exact import settings for third-party assets. Never treat an unverified free download as unrestricted.
4. For pixel art: test pixel snapping, filtering, scaling and sprite boundaries; check frame size, pivots, loop seams, direction ordering and background transparency.
5. For isometric scenes: document tile footprint, world-to-screen projection, z-order/occlusion and collision assumptions. Verify depth ordering with moving characters rather than a static screenshot.
6. For UI: check multiple aspect ratios, touch hit areas, text legibility and localization overflow if applicable.
7. Deliver preview evidence: actual Godot scene screenshot/video/GIF where possible, plus project paths. If not run, explicitly mark "not visually verified" and explain how to inspect.

Update a durable art/design decision only when it affects future consistency; avoid copying per-frame observations into long-lived rules.
