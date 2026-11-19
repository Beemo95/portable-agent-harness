"""The adapter must never treat planning progress as verified implementation."""
from pathlib import Path
import json
import tempfile
import unittest
from unittest.mock import patch

from harness.openspec_bridge import list_changes, status, packet, change_dir, _openspec_json


class OpenSpecBridgeTests(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory()
        self.root = Path(self.t.name)
        self.change = self.root / 'openspec' / 'changes' / 'add-feature'
        self.change.mkdir(parents=True)
        (self.change / 'proposal.md').write_text('# Proposal\n', encoding='utf-8')

    def tearDown(self):
        self.t.cleanup()

    def test_empty_changes_and_no_tasks_are_not_complete(self):
        state = status(self.root, 'add-feature', include_cli=False)
        self.assertFalse(state['implementation_complete'])
        self.assertFalse(state['implementation_verified'])
        self.assertIsNone(state['tasks']['next_unchecked'])
        self.assertEqual(len(list_changes(self.root)['changes']), 1)

    def test_checklist_is_read_only_and_reports_pending(self):
        body = '# Implementation\n- [x] Completed\n- [ ] Do the next thing\n* [-] Skipped\n- [ ] Later task\n'
        path = self.change / 'tasks.md'
        path.write_text(body, encoding='utf-8')
        result = status(self.root, 'add-feature', include_cli=False)
        self.assertEqual({k: result['tasks'][k] for k in ['total','completed','pending','skipped']},
                         {'total':4,'completed':1,'pending':2,'skipped':1})
        self.assertEqual(result['tasks']['next_unchecked'], 'Do the next thing')
        self.assertEqual(packet(self.root, 'add-feature', include_cli=False)['next_unchecked'], 'Do the next thing')
        self.assertEqual(path.read_text(encoding='utf-8'), body)

    def test_planning_complete_not_mistaken_for_implementation(self):
        (self.change / 'tasks.md').write_text('- [ ] Implement\n', encoding='utf-8')
        from unittest.mock import patch
        with patch('harness.openspec_bridge._openspec_json', return_value=({'isPlanningComplete': True}, None)):
            result = status(self.root, 'add-feature')
        self.assertTrue(result['planning_status']['isPlanningComplete'])
        self.assertFalse(result['implementation_complete'])
        self.assertFalse(result['implementation_verified'])

    def test_completed_checklist_still_not_verified(self):
        (self.change / 'tasks.md').write_text('- [x] Implemented\n', encoding='utf-8')
        result = status(self.root, 'add-feature', include_cli=False)
        self.assertTrue(result['implementation_complete'])
        self.assertFalse(result['implementation_verified'])

    def test_no_traversal_or_symlink(self):
        for name in ('../x', 'UPPER', 'not--valid', '.git'):
            with self.assertRaises(ValueError): change_dir(self.root, name)
        outside = self.root / 'external'; outside.mkdir()
        (self.root / 'openspec' / 'changes' / 'evil').symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError): change_dir(self.root, 'evil')
        self.assertNotIn('evil', [x['name'] for x in list_changes(self.root)['changes']])

    def test_missing_openspec_is_explicit(self):
        with patch('harness.openspec_bridge.shutil.which', return_value=None):
            result, note = _openspec_json(self.root, ['list', '--json'])
        self.assertIsNone(result)
        self.assertIn('unavailable', note)

    def test_cli_whitelist_arguments(self):
        (self.change / 'tasks.md').write_text('- [ ] Implement\n', encoding='utf-8')
        from subprocess import CompletedProcess
        with patch('harness.openspec_bridge.shutil.which', return_value='/usr/bin/openspec'):
            with patch('harness.openspec_bridge.subprocess.run', return_value=CompletedProcess([], 0, '{"isPlanningComplete":true}', '')) as run:
                result = status(self.root, 'add-feature')
        self.assertTrue(result['planning_status']['isPlanningComplete'])
        calls = [call for call in run.call_args_list if call.args[0][0] == '/usr/bin/openspec']
        self.assertEqual(len(calls), 1)
        command = calls[0].args[0]
        self.assertEqual(command, ['/usr/bin/openspec','status','--change','add-feature','--json'])
        self.assertFalse(calls[0].kwargs['check'])

if __name__ == '__main__':
    unittest.main()
