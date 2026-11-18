from pathlib import Path
import json
import tempfile
import unittest
from harness.install import install
from harness.config import load_config, gates_by_id
from harness.tasks import create_task, transition
from harness.verification import verify
from harness.util import write_json_atomic

ROOT = Path(__file__).resolve().parents[1]

class VerificationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'project'
        install(ROOT, self.root, 'Demo')
        self.tests = self.root / 'tests'; self.tests.mkdir()
        (self.tests / 'test_app.py').write_text(
            'import unittest\nclass AppTests(unittest.TestCase):\n'
            '    def test_true(self): self.assertTrue(True)\n', encoding='utf-8')
        self.cfg = load_config(self.root)
        self.cfg['verification']['gates'] = [{
            'id':'unit', 'argv':['{python}', '-m', 'unittest', 'discover', '-s', 'tests', '-v'],
            'min_tests':1, 'timeout_seconds':30, 'required':True}]
        write_json_atomic(self.root / 'project.harness.json', self.cfg)
        self.gates = gates_by_id(self.cfg)
        create_task(self.root, 'T-001', 'Test work', 'Should test feature', ['Should work'], ['unit'])
        transition(self.root, 'T-001', 'ready', 0, self.gates)
        transition(self.root, 'T-001', 'in_progress', 1, self.gates)

    def tearDown(self):
        self.temp.cleanup()

    def test_done_requires_current_gate(self):
        transition(self.root, 'T-001', 'verifying', 2, self.gates)
        with self.assertRaises(RuntimeError):
            transition(self.root, 'T-001', 'done', 3, self.gates)
        result = verify(self.root, self.cfg, 'T-001')
        self.assertTrue(result['all_passed'])
        self.assertEqual(result['results'][0]['test_count'], 1)
        self.assertEqual(transition(self.root, 'T-001', 'done', 3, self.gates)['status'], 'done')

    def test_old_evidence_is_rejected_after_source_change(self):
        transition(self.root, 'T-001', 'verifying', 2, self.gates)
        self.assertTrue(verify(self.root, self.cfg, 'T-001')['all_passed'])
        (self.root / 'src.py').write_text('x = 2\n', encoding='utf-8')
        with self.assertRaisesRegex(RuntimeError, 'changed since verification'):
            transition(self.root, 'T-001', 'done', 3, self.gates)

    def test_zero_tests_fails_min_tests(self):
        (self.tests / 'test_app.py').unlink()
        result = verify(self.root, self.cfg, 'T-001')
        self.assertFalse(result['all_passed'])
        self.assertEqual(result['results'][0]['test_count'], 0)

    def test_failure_has_actual_evidence(self):
        (self.tests / 'test_app.py').write_text('import unittest\nclass AppTests(unittest.TestCase):\n def test_bad(self): self.assertEqual(1, 2)\n', encoding='utf-8')
        result = verify(self.root, self.cfg, 'T-001')
        self.assertFalse(result['all_passed'])
        self.assertEqual(result['results'][0]['status'], 'fail')
        self.assertTrue((self.root / result['evidence_file']).exists())

if __name__ == '__main__':
    unittest.main()

class ContractTamperTests(unittest.TestCase):
    def test_contract_change_invalidates_prior_pass(self):
        from harness.tasks import create_task, transition
        with tempfile.TemporaryDirectory() as d:
            root = Path(d) / 'project'
            install(ROOT, root, 'Contract test')
            cfg = load_config(root)
            cfg['verification']['gates'] = [{'id':'unit', 'argv':['{python}','-c','print("ok")'], 'required':True}]
            write_json_atomic(root / 'project.harness.json', cfg)
            gates = gates_by_id(cfg)
            create_task(root, 'T-002', 'Contract test', 'Work', ['Criterion A'], ['unit'])
            transition(root, 'T-002', 'ready', 0, gates)
            transition(root, 'T-002', 'in_progress', 1, gates)
            transition(root, 'T-002', 'verifying', 2, gates)
            self.assertTrue(verify(root, cfg, 'T-002')['all_passed'])
            path = root / '.harness' / 'tasks' / 'T-002' / 'contract.json'
            contract = json.loads(path.read_text(encoding='utf-8'))
            contract['acceptance'][0]['criterion'] = 'Different criterion B'
            write_json_atomic(path, contract)
            with self.assertRaisesRegex(RuntimeError, 'contract changed'):
                transition(root, 'T-002', 'done', 3, gates)
