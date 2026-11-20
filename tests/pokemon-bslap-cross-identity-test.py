import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch
SOURCE = Path(__file__).resolve().parents[1] / 'overlay/projects/ROCKNIX/packages/misc/butterflyos-pokemon/sources/butterflyos-bslap.py'
spec = importlib.util.spec_from_file_location('bslap_cross', SOURCE)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)

class CrossIdentityTests(unittest.TestCase):
    def runtime(self, frontend='a', core='b'):
        return SimpleNamespace(ID='gambatte-netpacket', FRONTEND_SHA=frontend*64, CORE_SHA=core*64)

    def test_game_boy_pair_ignores_unrelated_gba_build(self):
        with patch.object(app, 'gb_backend', return_value=self.runtime()):
            first = app.link_identity('G1RE')
            with patch.object(app, 'BACKEND', 'different-platform-gba-runtime'), patch.object(app, 'CORE_SHA', 'f'*64):
                self.assertEqual(app.link_identity('G1BL'), first)
                self.assertEqual(app.link_identity('G2CR'), first)
                self.assertEqual(app.link_identity('BPRE'), 'different-platform-gba-runtime')

    def test_changed_frontend_or_core_cannot_pair(self):
        with patch.object(app, 'gb_backend', return_value=self.runtime()):
            original = app.link_identity('G1RE')
        for runtime in (self.runtime('c','b'), self.runtime('a','c')):
            with patch.object(app, 'gb_backend', return_value=runtime):
                self.assertNotEqual(app.link_identity('G1RE'), original)

    def test_pinned_gba_builds_share_only_the_audited_profile(self):
        for frontend, core in app.GBA_LINK_RUNTIMES:
            with patch.object(app, 'FRONTEND_SHA', frontend), patch.object(app, 'CORE_SHA', core):
                self.assertEqual(app.link_identity('BPRE'), app.GBA_LINK_PROFILE)
                self.assertEqual(app.link_identity('BPEE'), app.GBA_LINK_PROFILE)
                with patch.object(app, 'CORE_SHA', 'f'*64):
                    self.assertEqual(app.link_identity('BPRE'), app.BACKEND)
                with patch.object(app, 'FRONTEND_SHA', 'f'*64):
                    self.assertEqual(app.link_identity('BPRE'), app.BACKEND)

    def test_sameboy_fallback_keeps_legacy_gate(self):
        with patch.object(app, 'gb_backend', return_value=SimpleNamespace(ID='sameboy-dual')):
            self.assertEqual(app.link_identity('G1RE'), app.BACKEND)

if __name__ == '__main__':
    unittest.main()
