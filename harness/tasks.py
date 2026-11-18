"""Versioned task contracts/checkpoints/handoffs kept inside Git."""
from __future__ import annotations
import json
from pathlib import Path
from .util import (now, read_json, write_json_atomic, exclusive_lock, git_head,
                   git_changes, source_fingerprint, valid_task_id)

TRANSITIONS = {
    'backlog': {'ready', 'blocked'},
    'ready': {'in_progress', 'blocked'},
    'in_progress': {'verifying', 'blocked'},
    'verifying': {'done', 'changes_requested', 'blocked'},
    'changes_requested': {'in_progress', 'blocked'},
    'blocked': {'ready', 'in_progress'},
    'done': set(),
}


def task_dir(root: Path, task_id: str) -> Path:
    return root / '.harness' / 'tasks' / valid_task_id(task_id)


def load_task(root: Path, task_id: str) -> tuple[dict, dict]:
    directory = task_dir(root, task_id)
    if not (directory / 'contract.json').exists() or not (directory / 'state.json').exists():
        raise FileNotFoundError(f'Unknown task {task_id}')
    return read_json(directory / 'contract.json'), read_json(directory / 'state.json')


def list_tasks(root: Path) -> list[dict]:
    base = root / '.harness' / 'tasks'
    if not base.exists():
        return []
    found = []
    for directory in sorted(base.iterdir()):
        if not directory.is_dir() or not (directory / 'state.json').is_file():
            continue
        contract, state = load_task(root, directory.name)
        found.append({'id': contract['id'], 'title': contract['title'], 'status': state['status'],
                      'revision': state['revision'], 'next_action': state.get('next_action')})
    return found


def append_event(directory: Path, event: dict) -> None:
    with (directory / 'events.jsonl').open('a', encoding='utf-8') as f:
        f.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + '\n')
        f.flush()


def create_task(root: Path, task_id: str, title: str, goal: str, acceptance: list[str], gate_ids: list[str]):
    if not title.strip() or not goal.strip():
        raise ValueError('Task title and goal cannot be empty')
    if not acceptance:
        raise ValueError('Provide at least one acceptance criterion with --accept')
    valid_task_id(task_id)
    directory = task_dir(root, task_id)
    if directory.exists():
        raise FileExistsError(f'Task already exists: {task_id}')
    directory.mkdir(parents=True)
    contract = {
        'schema_version': 1, 'id': task_id, 'title': title.strip(), 'goal': goal.strip(),
        'created_at': now(), 'scope': [], 'out_of_scope': [], 'references': [],
        'acceptance': [{'id': f'AC-{i:02d}', 'criterion': criterion, 'gate_ids': list(dict.fromkeys(gate_ids))}
                       for i, criterion in enumerate(acceptance, 1)],
        'approval_required': False,
    }
    state = {
        'schema_version': 1, 'task_id': task_id, 'revision': 0, 'status': 'backlog',
        'owner': None, 'completed': [], 'pending': [], 'blockers': [], 'next_action': None,
        'last_checkpoint': None, 'updated_at': now()
    }
    write_json_atomic(directory / 'contract.json', contract)
    write_json_atomic(directory / 'state.json', state)
    (directory / 'plan.md').write_text(
        '# Plan — ' + task_id + '\n\n## Verified facts & sources\n\n## Unknowns / product decisions\n\n'
        '## Small vertical slices (dependencies and owner)\n\n## Test and rollback strategy\n\n'
        'The approved acceptance criteria live in contract.json; do not duplicate or silently modify them.\n',
        encoding='utf-8')
    append_event(directory, {'type': 'created', 'time': now(), 'revision': 0})
    return contract


def assert_revision(state: dict, expected: int) -> None:
    if state['revision'] != expected:
        raise RuntimeError(f"Stale edit: expected revision {expected}, actual {state['revision']}. Re-read task.")


def check_ready(contract: dict, gates: dict):
    if not contract.get('acceptance'):
        raise RuntimeError('Cannot start: no acceptance criteria')
    for ac in contract['acceptance']:
        if not ac.get('gate_ids'):
            raise RuntimeError(f"{ac['id']} has no verification gates; configure contract first")
        missing = set(ac['gate_ids']) - set(gates)
        if missing:
            raise RuntimeError(f"{ac['id']} refers to missing gates {sorted(missing)}")


def transition(root: Path, task_id: str, to_status: str, expected: int, gates: dict, note: str = '') -> dict:
    directory = task_dir(root, task_id)
    with exclusive_lock(directory / '.write.lock'):
        contract, state = load_task(root, task_id)
        assert_revision(state, expected)
        previous = state['status']
        if to_status not in TRANSITIONS.get(previous, set()):
            raise ValueError(f'Invalid transition {previous} -> {to_status}')
        if to_status == 'ready':
            check_ready(contract, gates)
            if state.get('blockers'):
                raise RuntimeError('Cannot mark ready with unresolved blockers')
        if to_status == 'done':
            from .verification import check_done
            check_done(root, task_id, contract, state, gates)
        state['status'] = to_status
        state['revision'] += 1
        state['updated_at'] = now()
        write_json_atomic(directory / 'state.json', state)
        append_event(directory, {'type': 'transition', 'from': previous, 'to': to_status,
                                 'revision': state['revision'], 'time': now(), 'note': note})
        return state


def update_state(root: Path, task_id: str, expected: int, *, next_action: str | None = None,
                 completed: str | None = None, blocker: str | None = None, owner: str | None = None,
                 resolve_blocker: str | None = None, pending: str | None = None,
                 resolve_pending: str | None = None):
    directory = task_dir(root, task_id)
    with exclusive_lock(directory / '.write.lock'):
        _, state = load_task(root, task_id)
        assert_revision(state, expected)
        if next_action is not None:
            state['next_action'] = next_action
        if completed is not None:
            state['completed'].append(completed)
        if blocker is not None:
            state['blockers'].append(blocker)
        if owner is not None:
            state['owner'] = owner
        if resolve_blocker is not None:
            if resolve_blocker not in state['blockers']:
                raise ValueError(f'Blocker not found: {resolve_blocker}')
            state['blockers'].remove(resolve_blocker)
        if pending is not None:
            state['pending'].append(pending)
        if resolve_pending is not None:
            if resolve_pending not in state['pending']:
                raise ValueError(f'Pending item not found: {resolve_pending}')
            state['pending'].remove(resolve_pending)
        state['revision'] += 1
        state['updated_at'] = now()
        write_json_atomic(directory / 'state.json', state)
        append_event(directory, {'type': 'state_updated', 'revision': state['revision'], 'time': now(),
                                 'fields': [k for k, v in {'next_action': next_action, 'completed': completed,
                                      'blocker': blocker, 'owner': owner,
                                      'resolve_blocker': resolve_blocker, 'pending': pending,
                                      'resolve_pending': resolve_pending}.items() if v is not None]})
        return state


def checkpoint(root: Path, task_id: str, expected: int, note: str):
    directory = task_dir(root, task_id)
    with exclusive_lock(directory / '.write.lock'):
        _, state = load_task(root, task_id)
        assert_revision(state, expected)
        sha, file_count = source_fingerprint(root)
        new_revision = state['revision'] + 1
        dest = directory / 'checkpoints' / f'rev-{new_revision:05d}.json'
        cp = {'schema_version': 1, 'task_id': task_id, 'revision': new_revision,
              'time': now(), 'git_head': git_head(root), 'source_fingerprint': sha,
              'source_files': file_count, 'git_status': git_changes(root),
              'note': note, 'state': {**state, 'revision': new_revision}}
        write_json_atomic(dest, cp)
        state['revision'] = new_revision
        state['last_checkpoint'] = dest.relative_to(root).as_posix()
        state['updated_at'] = now()
        write_json_atomic(directory / 'state.json', state)
        append_event(directory, {'type': 'checkpoint', 'revision': new_revision,
                                 'time': now(), 'file': dest.relative_to(root).as_posix()})
        return cp


def get_resume(root: Path, task_id: str):
    contract, state = load_task(root, task_id)
    fingerprint, file_count = source_fingerprint(root)
    cp_path = state.get('last_checkpoint')
    cp = read_json(root / cp_path) if cp_path else None
    return {
        'task_id': task_id, 'goal': contract['goal'], 'status': state['status'],
        'revision': state['revision'], 'owner': state.get('owner'),
        'next_action': state.get('next_action'), 'completed': state.get('completed', []),
        'pending': state.get('pending', []), 'blockers': state.get('blockers', []),
        'acceptance': contract.get('acceptance', []), 'references': contract.get('references', []),
        'git_head': git_head(root), 'git_status': git_changes(root), 'source_files': file_count,
        'checkpoint': cp_path,
        'checkpoint_matches_current_sources': bool(cp and cp['source_fingerprint'] == fingerprint),
        'checkpoint_source_git_head': cp.get('git_head') if cp else None,
        'action': 'Reconcile current source with checkpoint and inspect referenced files before continuing',
    }


def handoff(root: Path, task_id: str) -> Path:
    info = get_resume(root, task_id)
    directory = task_dir(root, task_id)
    lines = [f'# Handoff — {task_id}', '', f"Goal: {info['goal']}",
             f"Status: {info['status']} (revision {info['revision']})", f"Owner: {info['owner'] or '(unassigned)'}",
             f"Current Git HEAD: `{info['git_head'] or 'unavailable'}`",
             f"Checkpoint: `{info['checkpoint'] or '(none)'}`",
             f"Checkpoint matches current sources: **{info['checkpoint_matches_current_sources']}**",
             '', '## Completed']
    lines += [f'- {x}' for x in info['completed']] or ['- (none recorded)']
    lines += ['', '## Remaining', f"- {info['next_action'] or '(inspect task contract and choose next slice)'}"]
    lines += [f'- Blocker: {b}' for b in info['blockers']]
    lines += ['', '## Restart procedure',
              f'1. `python3 scripts/harness.py resume {task_id}`',
              f'2. `python3 scripts/harness.py context "{info["goal"].replace(chr(34), "")}" --task {task_id}`',
              '3. Inspect current code and compare checkpoint, Git status, and evidence.',
              '4. Continue only after reconciling any drift.',
              '', '## Git status', '```', info['git_status'], '```', '']
    path = directory / 'handoff.md'
    path.write_text('\n'.join(lines), encoding='utf-8')
    return path
