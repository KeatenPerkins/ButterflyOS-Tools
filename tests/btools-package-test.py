import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('package', REPO/'tools/btools/package.py')
p = importlib.util.module_from_spec(spec)
spec.loader.exec_module(p)

class PackagingTests(unittest.TestCase):
    def test_relocated_helpers_and_data_paths(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            native = root/'stage/usr/bin/butterflyos-save-trade'
            native.parent.mkdir(parents=True)
            native.write_text('#!/bin/sh\necho TEST\n');native.chmod(0o755)
            archive=root/'bdex.zip'
            p.build('bdex','1.0.0','rgds-plus',root/'stage',archive)
            with zipfile.ZipFile(archive) as bundle:
                bundle.extractall(root/'installed')
            binary=root/'installed/bin'
            code="""import btools_paths
from pathlib import Path
assert btools_paths.path('/usr/bin/butterflyos-save-trade') == str(Path(btools_paths.__file__).with_name('butterflyos-save-trade'))
assert btools_paths.path('/storage/bdex') == '/storage/bdex'
assert btools_paths.path('/usr/bin/control-gen_init.sh') == '/usr/bin/control-gen_init.sh'
import importlib.util
s=importlib.util.spec_from_file_location('bdex',Path(btools_paths.__file__).with_name('butterflyos-bdex.py'))
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
assert str(m.HELPER).startswith(str(Path(btools_paths.__file__).parent))
"""
            subprocess.run([sys.executable,'-c',code],cwd=binary,check=True)
            subprocess.run([sys.executable,'-m','compileall','-q',str(binary)],check=True)
            manifest=json.loads((root/'installed/manifest.json').read_text())
            self.assertEqual(manifest['platform'],'rgds-plus')
            self.assertIn('web',manifest['services'])
            with self.assertRaises(ValueError):p.build('bdex','1.0.0','unknown',root/'stage',archive)

if __name__=='__main__':unittest.main()
