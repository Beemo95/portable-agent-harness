"""Environment diagnostics and static harness consistency checks."""
from __future__ import annotations
import json
import os
import subprocess
from contextlib import closing
from pathlib import Path
import shutil
import sqlite3
import sys
from .config import load_config, gates_by_id
from .tasks import list_tasks, load_task, check_ready
from .util import git_head, read_json, relative_safe


def doctor(root: Path) -> dict:
    config = load_config(root)
    required = tuple(int(v) for v in config.get('environment', {}).get('python_min', '3.10').split('.')[:2])
    items = []
    items.append({'check': 'python', 'ok': sys.version_info[:2] >= required,
                  'detail': f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro} >= {required}'})
    is_git = shutil.which('git') is not None
    items.append({'check': 'git_binary', 'ok': is_git or not config.get('environment', {}).get('git_required', True),
                  'detail': 'available' if is_git else 'not installed'})
    items.append({'check': 'git_history', 'ok': git_head(root) is not None,
                  'detail': git_head(root) or 'not a committed Git checkout; transfer requires Git commit/push'})
    try:
        with closing(sqlite3.connect(':memory:')) as db:
            db.execute('CREATE VIRTUAL TABLE test USING fts5(body)')
        fts_ok = True
    except sqlite3.OperationalError:
        fts_ok = False
    items.append({'check': 'sqlite_fts5', 'ok': fts_ok, 'detail': 'available' if fts_ok else 'not compiled in'})
    items.append({'check': 'agent_entry', 'ok': (root / 'AGENTS.md').exists(), 'detail': 'AGENTS.md'})
    for spec in config.get('environment', {}).get('required_tools', []):
        if isinstance(spec, str):
            spec = {'command': spec}
        cmd = spec.get('command')
        binary = shutil.which(cmd) if isinstance(cmd, str) and cmd else None
        matched = bool(binary)
        detail = binary or 'not found'
        if binary and spec.get('version_prefix'):
            try:
                result = subprocess.run([binary, *spec.get('version_args', ['--version'])],
                                        capture_output=True, text=True, timeout=8)
                detail = (result.stdout or result.stderr).strip().splitlines()[0][:150]
                matched = result.returncode == 0 and str(spec['version_prefix']) in detail
            except (OSError, subprocess.TimeoutExpired, IndexError):
                matched = False
                detail = 'cannot determine version'
        items.append({'check': f'required:{cmd}', 'ok': matched, 'detail': detail})
    for tool in config.get('environment', {}).get('optional_tools', []):
        found = shutil.which(tool)
        items.append({'check': f'optional:{tool}', 'ok': bool(found), 'detail': found or 'not found', 'optional': True})
    return {'project': config['project']['name'], 'checks': items,
            'ready': all(item['ok'] for item in items if not item.get('optional') and item['check'] != 'git_history'),
            'notes': ['git_history is informative until first commit; make a commit before clean-clone handoff']}


def lint(root: Path) -> dict:
    cfg = load_config(root)
    errors = []
    warnings = []
    gate_ids = [g.get('id') for g in cfg.get('verification', {}).get('gates', [])]
    if len(gate_ids) != len(set(gate_ids)):
        errors.append('duplicate verification gate IDs')
    for gate in cfg.get('verification', {}).get('gates', []):
        if not gate.get('argv') or not isinstance(gate.get('argv'), list):
            errors.append(f'gate {gate.get("id")}: argv must be a nonempty list')
        if gate.get('min_tests') is not None and int(gate['min_tests']) < 1:
            errors.append(f'gate {gate.get("id")}: min_tests must be positive')
    try:
        routes = read_json(root / '.harness' / 'context-routes.json').get('routes', [])
        for route in routes:
            for path in route.get('documents', []) + route.get('paths', []):
                try:
                    if not relative_safe(root, path).is_file():
                        warnings.append(f'route {route["id"]}: missing hint {path}')
                except ValueError:
                    errors.append(f'route {route["id"]}: unsafe path {path}')
    except FileNotFoundError:
        errors.append('.harness/context-routes.json missing')
    if not (root / 'ai-docs' / 'INDEX.md').exists():
        warnings.append('ai-docs/INDEX.md missing')
    gates = gates_by_id(cfg)
    for task in list_tasks(root):
        contract, state = load_task(root, task['id'])
        if state['status'] not in {'backlog', 'blocked'}:
            try:
                check_ready(contract, gates)
            except RuntimeError as exc:
                errors.append(f'task {task["id"]}: {exc}')
        if state['status'] == 'done' and state.get('blockers'):
            errors.append(f'task {task["id"]}: marked done with blockers')
        if state['revision'] < 0:
            errors.append(f'task {task["id"]}: negative revision')
        directory = root / '.harness' / 'tasks' / task['id']
        events_path = directory / 'events.jsonl'
        try:
            entries = [json.loads(line) for line in events_path.read_text(encoding='utf-8').splitlines() if line.strip()]
            if not entries or entries[-1].get('revision') != state['revision']:
                errors.append(f'task {task["id"]}: state revision and latest event disagree')
        except (OSError, json.JSONDecodeError):
            errors.append(f'task {task["id"]}: missing/corrupt event log')
        if state.get('last_checkpoint'):
            try:
                if not relative_safe(root, state['last_checkpoint']).is_file():
                    errors.append(f'task {task["id"]}: checkpoint missing')
            except ValueError:
                errors.append(f'task {task["id"]}: checkpoint outside repo')
    for rel in ['CLAUDE.md', 'GEMINI.md']:
        path = root / rel
        if path.exists() and 'AGENTS.md' not in path.read_text(encoding='utf-8'):
            warnings.append(f'{rel} does not refer to AGENTS.md')
    if not gates:
        warnings.append('no verification gates configured; task completion is blocked until configured')
    return {'ok': not errors, 'errors': errors, 'warnings': warnings}
