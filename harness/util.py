"""Safe local file operations and repository fingerprinting."""
from __future__ import annotations
import contextlib
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from datetime import datetime, timezone

IGNORED_DIRS = {'.git', '.venv', 'venv', 'node_modules', '__pycache__', '.pytest_cache', 'dist', 'build', '.idea'}
IGNORED_FILES = {'.DS_Store'}
TASK_ID_RE = re.compile(r'^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$')


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec='seconds')


def read_json(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)


def write_json_atomic(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2) + '\n'
    fd, temp = tempfile.mkstemp(prefix=f'.{path.name}.', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(payload)
            f.flush()
            os.fsync(f.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


@contextlib.contextmanager
def exclusive_lock(path: Path):
    """Fail rather than silently overwriting concurrent task edits."""
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError as exc:
        raise RuntimeError(f'Concurrent task write or stale lock: {path}. Inspect before removing.') from exc
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(f'pid={os.getpid()} at={now()}\n')
        yield
    finally:
        path.unlink(missing_ok=True)


def git_output(root: Path, *args: str) -> str | None:
    try:
        p = subprocess.run(['git', *args], cwd=root, capture_output=True, text=True,
                           timeout=10, check=False)
        return p.stdout.strip() if p.returncode == 0 else None
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def git_head(root: Path) -> str | None:
    return git_output(root, 'rev-parse', 'HEAD')


def git_changes(root: Path) -> str:
    return git_output(root, 'status', '--short', '--untracked-files=normal') or '(none or no git)'


def relative_safe(root: Path, value: str) -> Path:
    """Prevent task-supplied paths from escaping the repo."""
    resolved = (root / value).resolve()
    try:
        resolved.relative_to(root.resolve())
    except ValueError as exc:
        raise ValueError(f'Path outside repository: {value}') from exc
    return resolved


def iter_project_files(root: Path):
    """Walk independently of Git to include uncommitted code and assets."""
    for base, dirs, files in os.walk(root, followlinks=False):
        base_path = Path(base)
        rel_parts = base_path.relative_to(root).parts
        dirs[:] = sorted(d for d in dirs if d not in IGNORED_DIRS
                         and not (rel_parts == ('.harness',) and d in {'cache', 'tmp', 'evidence', 'tasks'}))
        for filename in sorted(files):
            if filename in IGNORED_FILES or filename.endswith(('.pyc', '.pyo', '.swp', '~', '.lock')):
                continue
            path = base_path / filename
            if path.is_symlink() or not path.is_file():
                continue
            yield path


def source_fingerprint(root: Path) -> tuple[str, int]:
    """Digest current source contents, including untracked files. Task records/evidence/cache are excluded.

    Designed for portable correctness, not huge monorepo throughput. Additional exclude paths
    should be reviewed rather than silently dropping source changes.
    """
    h = hashlib.sha256()
    total = 0
    for path in iter_project_files(root):
        rel = path.relative_to(root).as_posix()
        if rel.startswith(('.harness/tasks/', '.harness/evidence/', '.harness/cache/', '.harness/tmp/')):
            continue
        if rel.startswith('reports/') or rel.endswith(('.log', '.sqlite', '.sqlite3')):
            continue
        if path.name == '.env' or path.name.startswith('.env.') or path.suffix.lower() in {'.pem', '.key', '.p12'}:
            continue
        h.update(rel.encode('utf-8') + b'\0')
        with path.open('rb') as f:
            while True:
                chunk = f.read(1024 * 1024)
                if not chunk:
                    break
                h.update(chunk)
        total += 1
    return h.hexdigest(), total


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8', errors='replace')).hexdigest()


def valid_task_id(task_id: str):
    if not TASK_ID_RE.fullmatch(task_id):
        raise ValueError('Task IDs must look like F-001 or GAME-042; uppercase letters/numbers/hyphens only')
    return task_id
