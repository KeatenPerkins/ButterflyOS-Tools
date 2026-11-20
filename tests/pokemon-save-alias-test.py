import importlib.util
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
SOURCE = Path(__file__).resolve().parents[1] / 'overlay/projects/ROCKNIX/packages/misc/butterflyos-pokemon/sources/butterflyos-save-trade-sdl.py'
spec = importlib.util.spec_from_file_location('blink_alias', SOURCE)
blink = importlib.util.module_from_spec(spec)
spec.loader.exec_module(blink)

class SaveAliasTests(unittest.TestCase):
    def test_alias_removed_but_independent_same_content_retained(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            real, alias, independent = [root / name for name in ('real.srm', 'alias.srm', 'independent.srm')]
            real.write_bytes(b'same save')
            os.link(real, alias)
            independent.write_bytes(b'same save')
            def walk(path):
                names = {'/storage/games-internal/roms': [independent.name],
                         '/storage/games-external/roms': [real.name],
                         '/storage/roms': [alias.name]}
                return [(str(root), [], names[path])]
            with patch.object(blink.os.path, 'isdir', return_value=True), patch.object(blink.os, 'walk', side_effect=walk):
                result = blink._find_saves()
            self.assertEqual(set(result), {str(real), str(independent)})

    def test_event_groups_follow_games_for_each_generation(self):
        expected = {1: 'GEN 1 GIFTS', 2: 'CRYSTAL EVENTS', 3: 'GEN 3 ISLAND EVENTS'}
        for generation, label in expected.items():
            menus = []
            def choose(front, title, prompt, items, **kwargs):
                menus.append(items)
                return None
            with patch.object(blink, 'generation_saves', return_value=[]), patch.object(blink, 'choose_list', side_effect=choose):
                getattr(blink, 'choose_gen%d_local_save' % generation)(None)
            self.assertIn(label, [row[0] for row in menus[0]])

if __name__ == '__main__':
    unittest.main()
