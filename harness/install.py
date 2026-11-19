"""Non-destructive adoption into a fresh or existing repository."""
from __future__ import annotations
from pathlib import Path
import json
import shutil
from .util import write_json_atomic


def project_files(template_root: Path):
    """Select runtime files, not demonstration tasks, tests, caches or Git history."""
    primary = ['AGENTS.md', 'CLAUDE.md', 'GEMINI.md', 'project.harness.json',
               'mise.toml', '.harness/context-routes.json', '.harness/authority-map.json',
               '.github/copilot-instructions.md', '.cursor/rules/harness.mdc']
    for part in primary:
        yield Path(part)
    for subfolder in ('harness', 'scripts', 'docs', '.agent-docs', '.agents/skills',
                      '.claude/agents', 'openspec'):
        for path in sorted((template_root / subfolder).rglob('*')):
            if not path.is_file() or '__pycache__' in path.parts or path.suffix == '.pyc':
                continue
            # A template's own architectural decisions must not become the
            # new game's approved decisions.
            relative = path.relative_to(template_root)
            if relative.parts[:2] == ('.agent-docs', 'decisions'):
                continue
            yield relative


def install(template_root: Path, target: Path, name: str, *, dry_run=False):
    target = target.resolve()
    if not name.strip():
        raise ValueError('Nonempty --name required')
    paths = list(project_files(template_root))
    collisions = [str(p) for p in paths if (target / p).exists()]
    if collisions:
        raise RuntimeError('Refusing to overwrite existing files: ' + ', '.join(collisions[:20]) +
                           '. Merge deliberately or use an empty target directory.')
    if dry_run:
        return {'target': str(target), 'files_to_create': len(paths), 'collisions': [], 'dry_run': True}
    target.mkdir(parents=True, exist_ok=True)
    for part in paths:
        dst = target / part
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(template_root / part, dst)
    config_path = target / 'project.harness.json'
    config = json.loads(config_path.read_text(encoding='utf-8'))
    config['project'] = {'name': name, 'purpose': 'Fill in verified Godot game goals', 'kind': 'godot-game'}
    # No generic harness-selftest is accepted as evidence for application features.
    config['verification']['gates'] = []
    write_json_atomic(config_path, config)
    routes_path = target / '.harness' / 'context-routes.json'
    # Install portable, documentation-only Godot hints; exclude template's
    # implementation/test paths, which are not relevant to a new game.
    template_routes = json.loads((template_root / '.harness' / 'context-routes.json').read_text(encoding='utf-8'))
    game_routes = [route for route in template_routes.get('routes', [])
                   if route.get('id', '').startswith('godot-')]
    write_json_atomic(routes_path, {'schema_version': 1, 'routes': game_routes})
    (target / '.agent-docs' / 'product.md').write_text(
        '# Product intent\n\nDescribe user-approved goals and scope. Do not invent requirements.\n', encoding='utf-8')
    (target / '.agent-docs' / 'architecture.md').write_text(
        '# Project architecture\n\nInspect real project code and document known boundaries, risks and verification commands.\n',
        encoding='utf-8')
    # The snapshot is an index of observed project facts, not a fake game status.
    status = target / '.agent-docs' / 'STATUS.md'
    status.write_text(
        '# Current game project status\n\n'
        f'- **Project:** {name}\n'
        '- **Godot version/platform:** not inspected\n'
        '- **Active OpenSpec change(s):** none\n'
        '- **Implementation / test status:** not yet inspected or verified\n'
        '- **Blockers:** actual project structure and acceptance criteria unknown\n'
        '- **Next action:** inspect project.godot and affected scenes; update approved game specs\n'
        '- **Last updated:** initialize when actual work begins\n',
        encoding='utf-8')
    # OpenSpec owns requirements/change plans; do not auto-install or overwrite upstream skills.
    (target / '.harness' / 'tasks').mkdir(parents=True, exist_ok=True)
    (target / '.harness' / 'evidence').mkdir(parents=True, exist_ok=True)
    (target / '.harness' / '.gitignore').write_text('cache/\ntmp/\n*.lock\n', encoding='utf-8')
    return {'target': str(target), 'files_created': len(paths), 'next': [
        'Review project.harness.json and add real project test commands; task DONE is blocked without gates.',
        'Read AGENTS.md; configure .agent-docs/product.md, .agent-docs/architecture.md, and .agent-docs/STATUS.md from actual Godot files.',
        'Only if needed, initialize official OpenSpec tools after reviewing generated changes to bundled Skills and adapters.',
        'Run doctor and lint. Commit to Git to transfer to a new computer.']}
