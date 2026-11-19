"""Machine-collected quality-gate evidence, with stale-worktree detection."""
from __future__ import annotations
import re
import subprocess
import sys
import time
import uuid
from pathlib import Path
from .util import (now, write_json_atomic, read_json, source_fingerprint,
                   git_head, sha256_text)


def required_gate_ids(contract: dict) -> set[str]:
    return {gate for criterion in contract.get('acceptance', []) for gate in criterion.get('gate_ids', [])}


def verify(root: Path, config: dict, task_id: str | None = None, selected: list[str] | None = None):
    gates = {g['id']: g for g in config.get('verification', {}).get('gates', [])}
    contract_hash = None
    if task_id:
        from .tasks import load_task
        contract, _ = load_task(root, task_id)
        contract_hash = sha256_text((root / ".harness" / "tasks" / task_id / "contract.json").read_text(encoding="utf-8"))
        gate_ids = set(selected) if selected else required_gate_ids(contract)
        if not gate_ids:
            raise RuntimeError('Task has no mapped verification gates; set gate_ids in contract.json')
    else:
        gate_ids = set(selected) if selected else {g['id'] for g in gates.values() if g.get('required', True)}
    missing = gate_ids - set(gates)
    if missing:
        raise RuntimeError(f'Unknown gates: {sorted(missing)}')
    if not gate_ids:
        raise RuntimeError('No verification gates configured; do not claim success')
    before, count = source_fingerprint(root)
    results = []
    for gate_id in sorted(gate_ids):
        gate = gates[gate_id]
        argv = [str(x).replace('{python}', sys.executable) for x in gate.get('argv', [])]
        if not argv or not all(isinstance(arg, str) and arg for arg in argv):
            raise ValueError(f'Invalid argv for gate {gate_id}')
        record = {'gate_id': gate_id, 'argv': argv, 'started_at': now(),
                  'exit_code': None, 'test_count': None, 'status': 'error'}
        try:
            p = subprocess.run(argv, cwd=root, capture_output=True, text=True,
                               errors='replace', timeout=int(gate.get('timeout_seconds', 120)), check=False)
            record['exit_code'] = p.returncode
            record['stdout_sha256'] = sha256_text(p.stdout)
            record['stderr_sha256'] = sha256_text(p.stderr)
            combined = p.stdout + '\n' + p.stderr
            match = re.search(r'Ran (\d+) tests? in', combined)
            record['test_count'] = int(match.group(1)) if match else None
            # unittest includes skipped tests in 'Ran N tests'; a skip is not proof
            # that required verification executed. Be conservative by default.
            skip_match = re.search(r'OK\s*\([^)]*\bskipped=(\d+)\b[^)]*\)', combined)
            record['skipped_count'] = int(skip_match.group(1)) if skip_match else 0
            record['status'] = 'pass' if p.returncode == 0 else 'fail'
            if record['skipped_count'] > 0 and not gate.get('allow_skipped', False):
                record['status'] = 'fail'
                record['note'] = f'Gate reported {record["skipped_count"]} skipped tests; explicit allow_skipped required'
            min_tests = gate.get('min_tests')
            if min_tests is not None and (record['test_count'] is None or record['test_count'] < int(min_tests)):
                record['status'] = 'fail'
                record['note'] = f'Expected at least {min_tests} reported tests, got {record["test_count"]}'
            if p.returncode or record['status'] == 'fail':
                record['failure_excerpt'] = combined[-1800:]
        except subprocess.TimeoutExpired:
            record['status'] = 'timeout'
            record['note'] = f"timeout after {gate.get('timeout_seconds', 120)} seconds"
        except OSError as exc:
            record['note'] = str(exc)
        record['finished_at'] = now()
        results.append(record)
    after, after_count = source_fingerprint(root)
    if before != after:
        for result in results:
            if result['status'] == 'pass':
                result['status'] = 'stale'
                result['note'] = 'Source tree changed during verification'
    payload = {'schema_version': 1, 'run_id': f'{time.time_ns()}-{uuid.uuid4().hex[:8]}',
               'task_id': task_id, 'contract_sha256': contract_hash, 'recorded_at': now(), 'git_head': git_head(root),
               'source_fingerprint': after, 'source_file_count': after_count,
               'all_passed': all(x['status'] == 'pass' for x in results), 'results': results,
               'warning': 'This records command execution, not the semantic correctness of acceptance criteria.'}
    location = root / '.harness' / 'evidence' / (task_id or '_project') / (payload['run_id'] + '.json')
    write_json_atomic(location, payload)
    payload['evidence_file'] = location.relative_to(root).as_posix()
    return payload


def find_latest_evidence(root: Path, task_id: str):
    base = root / '.harness' / 'evidence' / task_id
    files = sorted(base.glob('*.json')) if base.exists() else []
    return (read_json(files[-1]), files[-1]) if files else (None, None)


def check_done(root: Path, task_id: str, contract: dict, state: dict, gates: dict):
    from .tasks import check_ready
    check_ready(contract, gates)
    if state.get('blockers'):
        raise RuntimeError('Cannot close task with unresolved blockers')
    if state.get('pending'):
        raise RuntimeError('Cannot close task with unfinished pending slices')
    if contract.get('approval_required'):
        raise RuntimeError('Human approval required. v1 does not auto-sign approvals.')
    required = required_gate_ids(contract)
    if not required:
        raise RuntimeError('No validation gates in acceptance criteria')
    evidence, path = find_latest_evidence(root, task_id)
    if not evidence:
        raise RuntimeError('No tool-generated verification evidence for this task')
    if not evidence.get('all_passed'):
        raise RuntimeError(f'Latest verification failed: {path}')
    current_contract_hash = sha256_text((root / '.harness' / 'tasks' / task_id / 'contract.json').read_text(encoding='utf-8'))
    if evidence.get('contract_sha256') != current_contract_hash:
        raise RuntimeError('Task contract changed since verification; re-run verify')
    observed = {r['gate_id'] for r in evidence['results'] if r['status'] == 'pass'}
    if not required.issubset(observed):
        raise RuntimeError(f'Missing passing gates: {sorted(required - observed)}')
    current, _ = source_fingerprint(root)
    if current != evidence['source_fingerprint']:
        raise RuntimeError('Code/docs changed since verification; re-run verify')
    if evidence['git_head'] != git_head(root):
        raise RuntimeError('Git HEAD changed since verification; re-run verify')
    return True
