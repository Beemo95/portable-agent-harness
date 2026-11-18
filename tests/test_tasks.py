import json
from pathlib import Path
import tempfile
import unittest
from harness.install import install
from harness.tasks import create_task, load_task, transition, checkpoint, get_resume, update_state, handoff
from harness.config import load_config, gates_by_id
from harness.util import write_json_atomic

ROOT = Path(__file__).resolve().parents[1]

class TaskLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'project'
        install(ROOT, self.root, 'Demo project')
        cfg = load_config(self.root)
        cfg['verification']['gates'] = [{'id': 'unit', 'argv': ['{python}', '-c', 'print("ok")'], 'required': True}]
        write_json_atomic(self.root / 'project.harness.json', cfg)
        self.gates = gates_by_id(cfg)

    def tearDown(self):
        self.temp.cleanup()

    def test_revision_and_allowed_transitions(self):
        create_task(self.root, 'F-001', 'Feature', 'Build thing', ['acceptance'], ['unit'])
        self.assertEqual(transition(self.root, 'F-001', 'ready', 0, self.gates)['revision'], 1)
        with self.assertRaises(RuntimeError):
            transition(self.root, 'F-001', 'in_progress', 0, self.gates)
        self.assertEqual(transition(self.root, 'F-001', 'in_progress', 1, self.gates)['revision'], 2)
        with self.assertRaises(ValueError):
            transition(self.root, 'F-001', 'done', 2, self.gates)

    def test_no_gate_prevents_ready(self):
        create_task(self.root, 'F-002', 'Feature', 'Build thing', ['criterion'], [])
        with self.assertRaises(RuntimeError):
            transition(self.root, 'F-002', 'ready', 0, self.gates)

    def test_checkpoint_detects_code_drift(self):
        create_task(self.root, 'F-003', 'Feature', 'Build thing', ['criterion'], ['unit'])
        transition(self.root, 'F-003', 'ready', 0, self.gates)
        transition(self.root, 'F-003', 'in_progress', 1, self.gates)
        cp = checkpoint(self.root, 'F-003', 2, 'before source changed')
        self.assertEqual(cp['revision'], 3)
        self.assertTrue(get_resume(self.root, 'F-003')['checkpoint_matches_current_sources'])
        (self.root / 'new-feature.py').write_text('print(42)\n', encoding='utf-8')
        self.assertFalse(get_resume(self.root, 'F-003')['checkpoint_matches_current_sources'])
        self.assertTrue(handoff(self.root, 'F-003').is_file())

    def test_state_update_has_cas(self):
        create_task(self.root, 'F-004', 'Feature', 'Build thing', ['criterion'], ['unit'])
        state = update_state(self.root, 'F-004', 0, next_action='inspect code', owner='developer')
        self.assertEqual(state['revision'], 1)
        self.assertEqual(load_task(self.root, 'F-004')[1]['next_action'], 'inspect code')
        with self.assertRaises(RuntimeError):
            update_state(self.root, 'F-004', 0, owner='qa')

    def test_blocker_can_be_resolved(self):
        create_task(self.root, 'F-005', 'Blocked', 'Fix dependency', ['criterion'], ['unit'])
        update_state(self.root, 'F-005', 0, blocker='missing access')
        with self.assertRaises(RuntimeError):
            transition(self.root, 'F-005', 'ready', 1, self.gates)
        state = update_state(self.root, 'F-005', 1, resolve_blocker='missing access')
        self.assertFalse(state['blockers'])
        self.assertEqual(transition(self.root, 'F-005', 'ready', 2, self.gates)['status'], 'ready')

    def test_task_id_path_traversal_rejected(self):
        with self.assertRaises(ValueError):
            create_task(self.root, '../../other', 't', 'g', ['a'], ['unit'])

if __name__ == '__main__':
    unittest.main()
