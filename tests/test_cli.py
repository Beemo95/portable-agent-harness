import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CliTests(unittest.TestCase):
    def call(self, *args):
        return subprocess.run([sys.executable, str(ROOT / 'scripts' / 'harness.py'), '--json', *args],
                              cwd=ROOT, capture_output=True, text=True, timeout=60)

    def test_doctor_and_lint(self):
        result = self.call('doctor')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)['ready'])
        result = self.call('lint')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)['ok'])

    def test_workflow_list_without_optional_upstream_cli(self):
        result = self.call('workflow', 'list')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['provider'], 'openspec')

    def test_context_outputs_current_source(self):
        result = self.call('context', 'verification checkpoint')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)['references'])

if __name__ == '__main__':
    unittest.main()
