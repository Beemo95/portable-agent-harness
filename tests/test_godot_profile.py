"""Structural checks for the Godot-first documentation profile, not game QA."""
from pathlib import Path
import re
import tempfile
import unittest

from harness.install import install
from harness.checks import lint
from harness.config import load_config

ROOT = Path(__file__).resolve().parents[1]
ROLES = {'director', 'developer', 'artist', 'qa', 'researcher'}
GODOT_SKILLS = {
    'godot-game-spec', 'godot-feature-implementation', 'godot-art-pipeline',
    'godot-debugging', 'godot-qa-playtest', 'research-and-evidence',
    'game-work-handoff',
}


class GodotProfileTests(unittest.TestCase):
    def test_short_router_links_existing_documents(self):
        entry = ROOT / 'AGENTS.md'
        body = entry.read_text(encoding='utf-8')
        self.assertLess(len(body.splitlines()), 65)
        links = re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', body)
        self.assertGreaterEqual(len(links), 12)
        for link in links:
            self.assertTrue((ROOT / link).exists(), f'Broken AGENTS.md link: {link}')
        self.assertIn('only', body.lower())

    def test_role_briefs_and_claude_adapters_are_distinct(self):
        for role in ROLES:
            source = ROOT / '.agent-docs' / 'agents' / f'{role}.md'
            adapter = ROOT / '.claude' / 'agents' / f'godot-{role}.md'
            self.assertTrue(source.is_file(), str(source))
            self.assertTrue(adapter.is_file(), str(adapter))
            body = adapter.read_text(encoding='utf-8')
            self.assertTrue(body.startswith('---\n'))
            self.assertIn(f'name: godot-{role}', body)
            self.assertIn(f'.agent-docs/agents/{role}.md', body)

    def test_bundled_skill_frontmatters(self):
        seen = set()
        for skill in (ROOT / '.agents' / 'skills').glob('*/SKILL.md'):
            text = skill.read_text(encoding='utf-8')
            self.assertTrue(text.startswith('---\n'), str(skill))
            header = text.split('---\n', 2)[1]
            fields = dict(line.split(': ', 1) for line in header.splitlines() if ': ' in line)
            self.assertEqual(fields.get('name'), skill.parent.name)
            self.assertTrue(fields.get('description'))
            self.assertLessEqual(len(fields['description']), 1024)
            self.assertNotIn(skill.parent.name, seen)
            seen.add(skill.parent.name)
        self.assertTrue(GODOT_SKILLS.issubset(seen))

    def test_godot_profile_installs_without_fake_game_claims(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'new-game'
            install(ROOT, target, 'Test Godot Game')
            for role in ROLES:
                self.assertTrue((target / '.agent-docs' / 'agents' / f'{role}.md').is_file())
                self.assertTrue((target / '.claude' / 'agents' / f'godot-{role}.md').is_file())
            for skill in GODOT_SKILLS:
                self.assertTrue((target / '.agents' / 'skills' / skill / 'SKILL.md').is_file())
            for rule in ('workflow', 'specification', 'research', 'development', 'design-art',
                         'debugging', 'verification', 'documentation'):
                self.assertTrue((target / '.agent-docs' / 'rules' / f'{rule}.md').is_file())
            cfg = load_config(target)
            self.assertEqual(cfg['project']['kind'], 'godot-game')
            import json
            routes = json.loads((target / '.harness' / 'context-routes.json').read_text(encoding='utf-8'))['routes']
            self.assertGreaterEqual(len(routes), 6)
            self.assertTrue(all(r['id'].startswith('godot-') for r in routes))
            self.assertFalse(cfg['verification']['gates'])
            self.assertFalse((target / 'project.godot').exists())
            self.assertIn('not yet inspected or verified',
                          (target / '.agent-docs' / 'STATUS.md').read_text(encoding='utf-8'))
            self.assertFalse((target / '.agent-docs' / 'decisions' / '0001-repo-native.md').exists())
            self.assertTrue(lint(target)['ok'])
            self.assertFalse((target / 'project').exists())
            self.assertFalse((target / 'ai-docs').exists())
            self.assertTrue((target / '.agent-docs' / 'INDEX.md').exists())

    def test_agent_docs_directory_is_single_source_for_harness_docs(self):
        self.assertFalse((ROOT / ("ai" + "-docs")).exists())
        self.assertFalse((ROOT / 'project').exists())
        self.assertTrue((ROOT / '.agent-docs' / 'INDEX.md').is_file())
        self.assertTrue((ROOT / '.agent-docs' / 'STATUS.md').is_file())
        self.assertFalse((ROOT / '.agent-docs' / '.agent-docs').exists())
        for rel in ('AGENTS.md', '.harness/context-routes.json',
                    '.harness/authority-map.json', 'harness/install.py',
                    'harness/checks.py'):
            self.assertNotIn('ai' + '-docs', (ROOT / rel).read_text(encoding='utf-8'))
        index = (ROOT / '.agent-docs' / 'INDEX.md').read_text(encoding='utf-8')
        for link in re.findall(r'\]\(([^)#]+)(?:#[^)]*)?\)', index):
            self.assertTrue((ROOT / '.agent-docs' / link).exists(), f'Broken .agent-docs/INDEX.md link: {link}')

    def test_only_approved_authority_for_plans(self):
        index = (ROOT / '.agent-docs' / 'INDEX.md').read_text(encoding='utf-8')
        self.assertIn('openspec/specs/', index)
        self.assertIn('openspec/changes/', index)
        self.assertTrue((ROOT / '.agent-docs' / 'STATUS.md').is_file())
        self.assertTrue((ROOT / 'docs' / 'godot-profile.md').is_file())

if __name__ == '__main__':
    unittest.main()
