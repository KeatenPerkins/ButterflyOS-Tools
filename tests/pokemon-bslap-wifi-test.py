import importlib.util
from pathlib import Path
from types import SimpleNamespace
import unittest
from unittest.mock import patch
SOURCE = Path(__file__).resolve().parents[1] / 'overlay/projects/ROCKNIX/packages/misc/butterflyos-pokemon/sources/butterflyos-bslap.py'
spec = importlib.util.spec_from_file_location('bslap_wifi', SOURCE)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)

class WifiTests(unittest.TestCase):
    def run_session(self, state='on', failed=False, raises=False):
        calls = []
        def run(arguments, **kwargs):
            calls.append(arguments[1:])
            if arguments[1:] == ['dev']:
                return SimpleNamespace(returncode=0, stdout='phy#0\n Interface wlan0\n type managed\n Interface p2p0\n type P2P-device\n')
            if 'get' in arguments:
                return SimpleNamespace(returncode=0, stdout='Power save: '+state+'\n')
            return SimpleNamespace(returncode=int(failed), stdout='')
        with patch.object(app.shutil, 'which', return_value='/usr/sbin/iw'), patch.object(app.subprocess, 'run', side_effect=run):
            try:
                with app.link_wifi_awake():
                    self.assertNotIn(['dev','wlan0','set','power_save','on'], calls)
                    if raises:raise RuntimeError('emulator launch failed')
            except RuntimeError:
                self.assertTrue(raises)
        return calls

    def test_enabled_is_disabled_then_restored(self):
        calls=self.run_session()
        self.assertEqual(calls[-2:], [['dev','wlan0','set','power_save','off'], ['dev','wlan0','set','power_save','on']])
        self.assertFalse(any('p2p0' in row for row in calls))

    def test_existing_off_stays_off(self):
        self.assertFalse(any('set' in row for row in self.run_session(state='off')))

    def test_launch_failure_restores_previous_setting(self):
        self.assertEqual(self.run_session(raises=True)[-1], ['dev','wlan0','set','power_save','on'])

    def test_failed_disable_does_not_change_original_setting(self):
        calls=self.run_session(failed=True)
        self.assertEqual(calls[-1], ['dev','wlan0','set','power_save','off'])

    def test_missing_iw_still_allows_link(self):
        with patch.object(app.shutil,'which',return_value=None), patch.object(app.subprocess,'run') as run:
            with app.link_wifi_awake():pass
        run.assert_not_called()

if __name__ == '__main__':unittest.main()
