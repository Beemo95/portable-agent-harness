from pathlib import Path
import tempfile
import unittest
from harness.install import install
from harness.config import load_config
from harness.context import build_packet
from harness.index import build_index, search
from harness.util import write_json_atomic

ROOT = Path(__file__).resolve().parents[1]

class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'project'
        install(ROOT, self.root, 'Demo')
        (self.root / 'src').mkdir()
        (self.root / 'src' / 'player.gd').write_text('class_name Player\nfunc do_isometric_movement():\n\tpass\n', encoding='utf-8')
        (self.root / '.agent-docs' / 'movement.md').write_text('# Movement\nIsometric character movement directions NE NW SE SW\n', encoding='utf-8')
        write_json_atomic(self.root / '.harness' / 'context-routes.json', {'schema_version': 1, 'routes': [
            {'id': 'movement', 'keywords': ['isometric', '이동'], 'documents': ['.agent-docs/movement.md'], 'paths': ['src/player.gd']}
        ]})
        self.cfg = load_config(self.root)

    def tearDown(self):
        self.temp.cleanup()

    def test_fts_index_and_incremental_update(self):
        self.assertGreaterEqual(build_index(self.root, self.cfg)['indexed_files'], 2)
        r = search(self.root, self.cfg, 'isometric movement')
        self.assertTrue(any(x['path'] in {'src/player.gd', '.agent-docs/movement.md'} for x in r))
        (self.root / 'src' / 'player.gd').write_text('func do_isometric_movement():\n\treturn 2\n', encoding='utf-8')
        stats = build_index(self.root, self.cfg)
        self.assertGreaterEqual(stats['updated_files'], 1)

    def test_packet_relevance_and_budget(self):
        p = build_packet(self.root, self.cfg, 'Fix isometric 이동 for character', budget_tokens=600)
        self.assertEqual(p['routes'], ['movement'])
        self.assertTrue(any(x['path'] == 'src/player.gd' for x in p['references']))
        self.assertFalse(any('nonexistent' in x['path'] for x in p['references']))

    def test_no_credentials_indexed(self):
        (self.root / '.env').write_text('ULTRA_SECRET_TOKEN=secret\n', encoding='utf-8')
        self.assertEqual(search(self.root, self.cfg, 'ULTRA_SECRET_TOKEN'), [])

if __name__ == '__main__':
    unittest.main()
