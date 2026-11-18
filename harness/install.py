"""Non-destructive adoption into a fresh or existing repository."""
from __future__ import annotations
from pathlib import Path
import json
import shutil
from .util import write_json_atomic


def project_files(template_root: Path):
    """Select runtime files, not demonstration tasks, tests, caches or Git history."""
    primary = ['AGENTS.md', 'CLAUDE.md', 'GEMINI.md', 'project.harness.json',
               'ai-docs/INDEX.md', 'ai-docs/product.md', 'ai-docs/architecture.md',
               '.harness/context-routes.json', '.harness/authority-map.json',
               '.github/copilot-instructions.md', '.cursor/rules/harness.mdc']
    for part in primary:
        yield Path(part)
    for subfolder in ('harness', 'scripts', 'docs', '.agents/skills'):
        for path in sorted((template_root / subfolder).rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
                yield path.relative_to(template_root)


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
    config['project'] = {'name': name, 'purpose': 'Fill in verified user-approved goal', 'kind': 'project'}
    # No generic harness-selftest is accepted as evidence for application features.
    config['verification']['gates'] = []
    write_json_atomic(config_path, config)
    routes_path = target / '.harness' / 'context-routes.json'
    write_json_atomic(routes_path, {'schema_version': 1, 'routes': []})
    (target / 'ai-docs' / 'product.md').write_text(
        '# Product intent\n\nDescribe user-approved goals and scope. Do not invent requirements.\n', encoding='utf-8')
    (target / 'ai-docs' / 'architecture.md').write_text(
        '# Project architecture\n\nInspect real project code and document known boundaries, risks and verification commands.\n',
        encoding='utf-8')
    (target / '.harness' / 'tasks').mkdir(parents=True, exist_ok=True)
    (target / '.harness' / 'evidence').mkdir(parents=True, exist_ok=True)
    (target / '.harness' / '.gitignore').write_text('cache/\ntmp/\n*.lock\n', encoding='utf-8')
    return {'target': str(target), 'files_created': len(paths), 'next': [
        'Review project.harness.json and add real project test commands; task DONE is blocked without gates.',
        'Fill ai-docs/product.md and ai-docs/architecture.md with verified information.',
        'Run doctor and lint. Commit to Git to transfer to a new computer.']}
