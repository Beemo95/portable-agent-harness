"""Config loading and portable project discovery."""
from __future__ import annotations
from pathlib import Path
from .util import read_json


def find_root(start: Path | None = None) -> Path:
    p = (start or Path.cwd()).resolve()
    for candidate in (p, *p.parents):
        if (candidate / 'project.harness.json').is_file():
            return candidate
    raise RuntimeError('No project.harness.json found. Run from a harness-enabled repository.')


def load_config(root: Path) -> dict:
    config = read_json(root / 'project.harness.json')
    if config.get('schema_version') != 1:
        raise ValueError('Unsupported project.harness.json schema_version (expected 1)')
    if not isinstance(config.get('project', {}).get('name'), str):
        raise ValueError('Missing project.name')
    if not isinstance(config.get('verification', {}).get('gates', []), list):
        raise ValueError('verification.gates must be an array')
    return config


def gates_by_id(config: dict) -> dict:
    return {x['id']: x for x in config.get('verification', {}).get('gates', [])}
