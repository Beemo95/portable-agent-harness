"""CLI: the public portable contract used by any agent/model."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from .config import find_root, load_config, gates_by_id
from .checks import doctor, lint
from .context import build_packet, render_packet
from .index import build_index, search
from .tasks import (create_task, list_tasks, load_task, transition, update_state,
                    checkpoint, handoff, get_resume)
from .verification import verify
from .install import install


def parse(argv=None):
    p = argparse.ArgumentParser(prog='harness', description='Portable project intelligence, execution state and verification')
    p.add_argument('--root', type=Path, help='override repository root')
    p.add_argument('--json', action='store_true', dest='json_output', help='machine-readable output')
    sp = p.add_subparsers(dest='command', required=True)
    sp.add_parser('doctor')
    sp.add_parser('lint')
    sp.add_parser('status')
    sp.add_parser('bootstrap').add_argument('--apply', action='store_true', help='run explicitly configured bootstrap commands')
    idx = sp.add_parser('index'); idx.add_argument('--rebuild', action='store_true')
    sea = sp.add_parser('search'); sea.add_argument('query'); sea.add_argument('--limit', type=int, default=8)
    ctx = sp.add_parser('context'); ctx.add_argument('query'); ctx.add_argument('--task'); ctx.add_argument('--budget', type=int)
    resume = sp.add_parser('resume'); resume.add_argument('task_id'); resume.add_argument('--budget', type=int)
    ver = sp.add_parser('verify'); ver.add_argument('task_id', nargs='?'); ver.add_argument('--gate', action='append')
    init = sp.add_parser('init'); init.add_argument('target', type=Path); init.add_argument('--name', required=True); init.add_argument('--dry-run', action='store_true')
    tasks = sp.add_parser('task'); tsp = tasks.add_subparsers(dest='task_command', required=True)
    tsp.add_parser('list')
    new = tsp.add_parser('new'); new.add_argument('task_id'); new.add_argument('--title', required=True); new.add_argument('--goal', required=True); new.add_argument('--accept', action='append', required=True); new.add_argument('--gate', action='append', default=[])
    show = tsp.add_parser('show'); show.add_argument('task_id')
    trans = tsp.add_parser('transition'); trans.add_argument('task_id'); trans.add_argument('status'); trans.add_argument('--expect', type=int, required=True); trans.add_argument('--note', default='')
    update = tsp.add_parser('update'); update.add_argument('task_id'); update.add_argument('--expect', type=int, required=True); update.add_argument('--next', dest='next_action'); update.add_argument('--completed'); update.add_argument('--blocker'); update.add_argument('--owner'); update.add_argument('--resolve-blocker'); update.add_argument('--pending'); update.add_argument('--resolve-pending')
    cp = tsp.add_parser('checkpoint'); cp.add_argument('task_id'); cp.add_argument('--expect', type=int, required=True); cp.add_argument('--note', required=True)
    ho = tsp.add_parser('handoff'); ho.add_argument('task_id')
    ev = sp.add_parser('eval'); evsp = ev.add_subparsers(dest='eval_command', required=True); evsp.add_parser('cold-start')
    return p.parse_args(argv)


def cold_start(root: Path):
    """Fresh local copy with no index/agent session; it cannot prove multi-model performance."""
    with tempfile.TemporaryDirectory(prefix='harness-cold-start-') as td:
        target = Path(td) / 'repo'
        shutil.copytree(root, target,
                        ignore=shutil.ignore_patterns('.git', '__pycache__', '.venv', 'node_modules', '*.pyc', '.pytest_cache', '.DS_Store'))
        shutil.rmtree(target / '.harness' / 'cache', ignore_errors=True)
        cmd = [sys.executable, str(target / 'scripts' / 'harness.py')]
        cases = [
            ('doctor', cmd + ['--json', 'doctor']),
            ('lint', cmd + ['--json', 'lint']),
            ('context', cmd + ['--json', 'context', 'task checkpoint and context search']),
        ]
        results = []
        for name, command in cases:
            p = subprocess.run(command, cwd=target, capture_output=True, text=True, timeout=45)
            try:
                parsed = json.loads(p.stdout)
            except json.JSONDecodeError:
                parsed = None
            ok = p.returncode == 0 and parsed is not None
            if name == 'doctor': ok = ok and parsed.get('ready', False)
            if name == 'lint': ok = ok and parsed.get('ok', False)
            if name == 'context': ok = ok and bool(parsed.get('references'))
            results.append({'case': name, 'passed': bool(ok),
                            'details': p.stderr[-400:] if not ok else 'ok'})
        return {'simulation': 'isolated directory copy, no prior index or agent session',
                'results': results, 'passed': all(x['passed'] for x in results),
                'limitations': 'Does not test clean Git clone, credentials, GUI, provider agent behavior, or semantic task success'}


def bootstrap(root: Path, cfg: dict, apply: bool):
    cmds = cfg.get('environment', {}).get('bootstrap_commands', [])
    if not apply:
        return {'mode': 'dry-run', 'commands': cmds, 'next': 'Review commands, then bootstrap --apply if trusted'}
    outputs = []
    for command in cmds:
        if not isinstance(command, list) or not command or not all(isinstance(x, str) for x in command):
            raise ValueError('bootstrap command must be nonempty argv string array (no shell)')
        args = [x.replace('{python}', sys.executable) for x in command]
        p = subprocess.run(args, cwd=root, capture_output=True, text=True, timeout=180)
        outputs.append({'argv': args, 'exit_code': p.returncode, 'stdout_tail': p.stdout[-400:], 'stderr_tail': p.stderr[-400:]})
        if p.returncode:
            break
    return {'mode': 'applied', 'results': outputs, 'passed': all(x['exit_code'] == 0 for x in outputs)}


def execute(args, root: Path):
    if args.command == 'init':
        return install(Path(__file__).resolve().parents[1], args.target, args.name, dry_run=args.dry_run)
    cfg = load_config(root)
    if args.command == 'doctor': return doctor(root)
    if args.command == 'lint': return lint(root)
    if args.command == 'status':
        from .util import git_changes, git_head
        return {'project': cfg['project']['name'], 'git_head': git_head(root),
                'git_status': git_changes(root), 'tasks': list_tasks(root)}
    if args.command == 'bootstrap': return bootstrap(root, cfg, args.apply)
    if args.command == 'index': return build_index(root, cfg, rebuild=args.rebuild)
    if args.command == 'search': return {'query': args.query, 'results': search(root, cfg, args.query, args.limit)}
    if args.command == 'context': return build_packet(root, cfg, args.query, args.task, args.budget)
    if args.command == 'resume':
        info = get_resume(root, args.task_id)
        return {'recovery': info, 'context': build_packet(root, cfg, info['goal'], args.task_id, args.budget)}
    if args.command == 'verify': return verify(root, cfg, args.task_id, args.gate)
    if args.command == 'eval': return cold_start(root)
    if args.command == 'task':
        task_cmd = args.task_command
        if task_cmd == 'list': return {'tasks': list_tasks(root)}
        if task_cmd == 'new': return create_task(root, args.task_id, args.title, args.goal, args.accept, args.gate)
        if task_cmd == 'show':
            contract, state = load_task(root, args.task_id)
            return {'contract': contract, 'state': state}
        if task_cmd == 'transition': return transition(root, args.task_id, args.status, args.expect, gates_by_id(cfg), args.note)
        if task_cmd == 'update': return update_state(root, args.task_id, args.expect, next_action=args.next_action, completed=args.completed, blocker=args.blocker, owner=args.owner,
                                                          resolve_blocker=args.resolve_blocker, pending=args.pending,
                                                          resolve_pending=args.resolve_pending)
        if task_cmd == 'checkpoint': return checkpoint(root, args.task_id, args.expect, args.note)
        if task_cmd == 'handoff': return {'handoff_file': str(handoff(root, args.task_id).relative_to(root))}
    raise ValueError(f'Unknown operation: {args.command}')


def main(argv=None):
    args = parse(argv)
    try:
        if args.command == 'init':
            # init is also supported from outside a harness-enabled repo.
            root = Path(__file__).resolve().parents[1]
        else:
            root = args.root.resolve() if args.root else find_root(Path.cwd())
        result = execute(args, root)
        if args.json_output:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        elif args.command == 'context':
            print(render_packet(result))
        elif args.command == 'resume':
            print('RECOVERY:\n' + json.dumps(result['recovery'], ensure_ascii=False, indent=2))
            print('\n' + render_packet(result['context']))
        else:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        if args.command == 'verify' and not result['all_passed']:
            return 2
        if args.command == 'lint' and not result['ok']:
            return 2
        if args.command == 'eval' and not result['passed']:
            return 2
        if args.command == 'bootstrap' and result.get('passed') is False:
            return 2
        return 0
    except (ValueError, FileNotFoundError, RuntimeError, OSError, KeyError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
