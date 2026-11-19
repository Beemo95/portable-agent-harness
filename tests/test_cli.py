import json
import os
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]

class CliTests(unittest.TestCase):
    def call(self, *args):
        return subprocess.run([sys.executable, str(ROOT / 'scripts' / 'harness.py'), '--json', *args],
                              cwd=ROOT, capture_output=True, text=True, encoding='utf-8', timeout=60)

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

    def test_utf8_output_even_if_default_codepage_cannot_encode_unicode(self):
        # Reproduce the Windows Actions failure (cp1252 cannot encode some
        # characters in indexed documentation), including when stdout is piped.
        env = dict(os.environ, PYTHONIOENCODING='cp1252')
        result = subprocess.run(
            [sys.executable, str(ROOT / 'scripts' / 'harness.py'),
             '--json', 'context', 'verification checkpoint'],
            cwd=ROOT, capture_output=True, text=True, encoding='utf-8',
            env=env, timeout=60)
        self.assertEqual(result.returncode, 0, result.stderr)
        response = json.loads(result.stdout)
        self.assertTrue(response['references'])
        self.assertNotIn('\ufffd', result.stdout)

if __name__ == '__main__':
    unittest.main()
