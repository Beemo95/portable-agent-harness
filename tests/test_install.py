from pathlib import Path
import tempfile
import unittest
from harness.checks import doctor, lint
from harness.config import load_config
from harness.install import install
from harness.context import build_packet

ROOT = Path(__file__).resolve().parents[1]

class BootstrapTests(unittest.TestCase):
    def test_install_without_overwrite_and_without_fake_app_tests(self):
        with tempfile.TemporaryDirectory() as d:
            target = Path(d) / 'new'
            self.assertTrue(install(ROOT, target, 'Fresh project', dry_run=True)['dry_run'])
            result = install(ROOT, target, 'Fresh project')
            self.assertGreater(result['files_created'], 10)
            cfg = load_config(target)
            self.assertEqual(cfg['project']['name'], 'Fresh project')
            self.assertEqual(cfg['verification']['gates'], [])
            self.assertEqual(cfg['workflow']['provider'], 'openspec')
            self.assertTrue((target / 'openspec' / 'config.yaml').is_file())
            self.assertTrue((target / 'mise.toml').is_file())
            self.assertTrue((target / '.agents' / 'skills' / 'openspec-pah-handoff' / 'SKILL.md').is_file())
            self.assertTrue(doctor(target)['ready'])
            self.assertTrue(lint(target)['ok'])
            with self.assertRaises(RuntimeError):
                install(ROOT, target, 'Different name')
            pkt = build_packet(target, cfg, 'bootstrap project work')
            self.assertTrue(pkt['references'])

if __name__ == '__main__':
    unittest.main()
