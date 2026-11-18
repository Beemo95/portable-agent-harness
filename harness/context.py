"""Build a small evidence-linked Context Packet, not an entire repository dump."""
from __future__ import annotations
import json
from pathlib import Path
from .index import search
from .tasks import load_task, get_resume, list_tasks
from .util import git_head, relative_safe, read_json


def route_matches(root: Path, query: str):
    routes_path = root / '.harness' / 'context-routes.json'
    if not routes_path.exists():
        return []
    routes = read_json(routes_path).get('routes', [])
    query_lower = query.lower()
    scored = []
    for route in routes:
        score = sum(1 for keyword in route.get('keywords', []) if keyword.lower() in query_lower)
        if score:
            scored.append((score, route))
    return [route for _, route in sorted(scored, key=lambda x: (-x[0], x[1]['id']))[:2]]


def build_packet(root: Path, config: dict, query: str, task_id: str | None = None,
                 budget_tokens: int | None = None) -> dict:
    budget = budget_tokens or config.get('retrieval', {}).get('default_context_tokens', 1800)
    if not 300 <= budget <= 20000:
        raise ValueError('context budget must be in 300..20000 tokens')
    combined = query
    task_info = None
    if task_id:
        contract, _ = load_task(root, task_id)
        full = get_resume(root, task_id)
        task_info = {
            'task_id': full['task_id'], 'status': full['status'], 'revision': full['revision'],
            'owner': full['owner'], 'next_action': str(full['next_action'] or '')[:160],
            'blockers': [str(x)[:120] for x in full['blockers'][:3]],
            'checkpoint': full['checkpoint'],
            'checkpoint_matches_current_sources': full['checkpoint_matches_current_sources'],
            'acceptance_refs': [x['id'] for x in full['acceptance'][:12]],
            'contract_path': f'.harness/tasks/{task_id}/contract.json'
        }
        combined += ' ' + contract['title'] + ' ' + contract['goal']
    routes = route_matches(root, combined)
    results = search(root, config, combined, limit=min(12, config.get('retrieval', {}).get('max_results', 8) + 4))
    prioritized = []
    for route in routes:
        for path in route.get('documents', []) + route.get('paths', []):
            try:
                absolute = relative_safe(root, path)
            except ValueError:
                continue
            if absolute.is_file():
                prioritized.append({'path': path, 'start_line': 1,
                                    'end_line': min(len(absolute.read_text(encoding='utf-8').splitlines()), 100),
                                    'excerpt': absolute.read_text(encoding='utf-8')[:500], 'origin': 'route'})
    for result in results:
        prioritized.append({**result, 'origin': 'search'})
    seen = set()
    references = []
    for item in prioritized:
        if item['path'] in seen:
            continue
        if item['path'].startswith(('.harness/cache/', '.env')):
            continue
        seen.add(item['path'])
        references.append(item)
    # Explicit budget: Korean text may need more tokens per character than English.
    # Account for fixed packet fields and short task state first. This is still only
    # a character-based approximation, not a tokenizer-exact budget.
    active_tasks = []
    if not task_id:
        query_words = [w.lower() for w in combined.split() if len(w) >= 2]
        candidates = [x for x in list_tasks(root) if x['status'] != 'done']
        ranked = sorted(candidates, key=lambda x: -sum(w in (x['title'] + ' ' + x['id']).lower() for w in query_words))
        active_tasks = [{'id': x['id'], 'title': x['title'][:70], 'status': x['status']} for x in ranked[:3]]
    fixed_cost = len(json.dumps({'project': config['project']['name'], 'goal': query[:150],
                                 'task_state': task_info, 'active_tasks': active_tasks}, ensure_ascii=False))
    remaining_chars = max(0, budget * 2 - fixed_cost - 250)
    context_refs = []
    for item in references:
        if remaining_chars < 140:
            break
        excerpt = item.get('excerpt', '')[:min(460, remaining_chars - 100)]
        context_refs.append({'path': item['path'], 'lines': [item['start_line'], item['end_line']],
                             'origin': item['origin'], 'excerpt': excerpt})
        remaining_chars -= len(excerpt) + len(item['path']) + 100
    return {'project': config['project']['name'], 'goal': query[:500], 'task_id': task_id,
            'git_head': git_head(root), 'routes': [x['id'] for x in routes],
            'task_state': task_info, 'active_tasks': active_tasks, 'references': context_refs,
            'budget_tokens_approx': budget, 'caveat': 'Paths and excerpts are leads; inspect current source before editing.'}


def render_packet(packet: dict) -> str:
    lines = [f"# Context Packet — {packet['project']}", f"Goal: {packet['goal']}",
             f"HEAD: {packet['git_head'] or '(unavailable)'}",
             f"Routes: {', '.join(packet['routes']) or '(fallback search)'}"]
    if packet.get('task_state'):
        info = packet['task_state']
        lines += ['', f"Task: {info['task_id']} | {info['status']} | revision {info['revision']}",
                  f"Next: {info.get('next_action') or '(inspect contract)'}",
                  f"Checkpoint reconciled: {info['checkpoint_matches_current_sources']}"]
        if info['blockers']:
            lines.append('Blockers: ' + '; '.join(info['blockers']))
    if packet.get('active_tasks'):
        lines += ['', '## Candidate active tasks (confirm before acting)']
        lines += [f"- {t['id']}: {t['title']} ({t['status']})" for t in packet['active_tasks']]
    lines += ['', '## Targeted sources (verify before use)']
    for r in packet['references']:
        lines += [f"- `{r['path']}:{r['lines'][0]}-{r['lines'][1]}` [{r['origin']}]",
                  f"  {r['excerpt'].replace(chr(10), ' ')[:350]}"]
    lines += ['', 'Do not treat excerpts or stale checkpoints as authoritative runtime state.']
    return '\n'.join(lines)
