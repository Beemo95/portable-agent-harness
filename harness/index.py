"""Local rebuildable FTS5 search cache. Source documents remain authoritative."""
from __future__ import annotations
import os
from contextlib import closing
from pathlib import Path
import re
import sqlite3
from .util import iter_project_files

BLACKLIST_FILES = {'AGENTS.md'}  # AGENTS is always included separately, not retrieved as a search result.
SENSITIVE_SUFFIXES = {'.pem', '.key', '.p12', '.db', '.sqlite', '.sqlite3', '.png', '.jpg', '.webp', '.pdf', '.zip'}


def allowed_file(root: Path, path: Path, config: dict) -> bool:
    rel = path.relative_to(root).as_posix()
    if rel.startswith(('.harness/cache/', '.harness/evidence/', '.git/', '.harness/tmp/')):
        return False
    if path.name in BLACKLIST_FILES or path.name == '.env' or path.name.startswith('.env.'):
        return False
    if path.suffix.lower() in SENSITIVE_SUFFIXES:
        return False
    if path.suffix.lower() not in config.get('retrieval', {}).get('extensions', []):
        return False
    return path.stat().st_size <= config.get('retrieval', {}).get('max_file_bytes', 180000)


def connect_db(root: Path):
    path = root / '.harness' / 'cache' / 'search.sqlite3'
    path.parent.mkdir(parents=True, exist_ok=True)
    db = sqlite3.connect(path, timeout=10)
    db.execute('PRAGMA busy_timeout=10000')
    db.execute('CREATE TABLE IF NOT EXISTS files (path TEXT PRIMARY KEY, mtime INTEGER, size INTEGER)')
    try:
        db.execute("CREATE VIRTUAL TABLE IF NOT EXISTS chunks USING fts5(path UNINDEXED, start_line UNINDEXED, end_line UNINDEXED, body, tokenize='unicode61')")
    except sqlite3.OperationalError as exc:
        db.close()
        raise RuntimeError('This Python sqlite3 build lacks FTS5; install one with SQLite FTS5 support') from exc
    return db


def chunks_of(content: str, chunk_lines: int = 60, overlap: int = 8):
    lines = content.splitlines()
    if not lines:
        return
    step = chunk_lines - overlap
    for pos in range(0, len(lines), step):
        piece = '\n'.join(lines[pos:pos + chunk_lines])
        if piece.strip():
            yield pos + 1, min(pos + chunk_lines, len(lines)), piece


def build_index(root: Path, config: dict, *, rebuild=False) -> dict:
    with closing(connect_db(root)) as db, db:
        if rebuild:
            db.execute('DELETE FROM chunks')
            db.execute('DELETE FROM files')
        old = {p: (mtime, size) for p, mtime, size in db.execute('SELECT path,mtime,size FROM files')}
        seen = set()
        updated = 0
        for path in iter_project_files(root):
            if not allowed_file(root, path, config):
                continue
            rel = path.relative_to(root).as_posix()
            seen.add(rel)
            stat = path.stat()
            key = (stat.st_mtime_ns, stat.st_size)
            if old.get(rel) == key:
                continue
            try:
                body = path.read_text(encoding='utf-8')
            except (UnicodeDecodeError, OSError):
                continue
            db.execute('DELETE FROM chunks WHERE path=?', (rel,))
            for start, end, piece in chunks_of(body):
                db.execute('INSERT INTO chunks(path,start_line,end_line,body) VALUES(?,?,?,?)',
                           (rel, start, end, piece))
            db.execute('INSERT OR REPLACE INTO files(path,mtime,size) VALUES(?,?,?)',
                       (rel, *key))
            updated += 1
        for stale in old.keys() - seen:
            db.execute('DELETE FROM chunks WHERE path=?', (stale,))
            db.execute('DELETE FROM files WHERE path=?', (stale,))
        return {'indexed_files': len(seen), 'updated_files': updated, 'deleted_files': len(old.keys() - seen)}


def search(root: Path, config: dict, query: str, limit: int | None = None):
    build_index(root, config)
    words = re.findall(r'[\w가-힣]+', query, flags=re.UNICODE)
    words = list(dict.fromkeys(x.lower() for x in words if len(x) >= 2))[:12]
    if not words:
        return []
    # Avoid user-provided FTS syntax, operator injection, and invalid queries.
    fts_query = ' OR '.join('"' + x.replace('"', '""') + '"' for x in words)
    with closing(connect_db(root)) as db:
        results = db.execute(
            'SELECT path,start_line,end_line,body,bm25(chunks) AS score FROM chunks '
            'WHERE chunks MATCH ? ORDER BY score LIMIT ?',
            (fts_query, max(1, min(limit or config.get('retrieval', {}).get('max_results', 8), 50)) * 4)).fetchall()
    out = []
    seen_paths = set()
    for path, start, end, content, score in results:
        if path in seen_paths:
            continue
        seen_paths.add(path)
        # Prefer a concise excerpt around the first matching term.
        lower = content.lower()
        offset = min((i for term in words if (i := lower.find(term)) >= 0), default=0)
        begin = max(0, offset - 140)
        excerpt = content[begin:begin + 550]
        out.append({'path': path, 'start_line': start, 'end_line': end,
                    'score': round(float(score), 4), 'excerpt': excerpt})
        if len(out) >= (limit or config.get('retrieval', {}).get('max_results', 8)):
            break
    return out
