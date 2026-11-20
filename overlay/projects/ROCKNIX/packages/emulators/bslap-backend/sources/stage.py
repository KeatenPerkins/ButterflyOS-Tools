#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path
import shutil
import sys
build, install = map(Path, sys.argv[1:])
files = {}
for package, target in (
    ('bslap-retroarch', '/usr/libexec/bslap/retroarch'),
    ('gpsp-bslap-lr', '/usr/lib/libretro/gpsp_bslap_libretro.so'),
    ('gambatte-bslap-lr', '/usr/lib/libretro/gambatte_bslap_libretro.so'),
    ('sameboy-lr', '/usr/lib/libretro/sameboy_libretro.so')):
    matches = list(build.glob(package + '-*/' + target.lstrip('/')))
    if len(matches) != 1:
        raise SystemExit('Expected one installed dependency: ' + package)
    files[target] = hashlib.sha256(matches[0].read_bytes()).hexdigest()
for core in ('gpsp', 'gambatte'):
    matches = list(build.glob('core-info-*/usr/lib/libretro/' + core + '_libretro.info'))
    if len(matches) != 1:
        raise SystemExit('Missing core metadata: ' + core)
    out = install / ('usr/lib/libretro/' + core + '_bslap_libretro.info')
    out.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(matches[0], out)
manifest = dict(schema=1, files=files, platform='rgds-plus-aarch64',
                frontend='/usr/libexec/bslap/retroarch', cross_device_qualified=False)
manifest['backend'] = 'rgds-bslap-v4-' + hashlib.sha256(json.dumps(files, sort_keys=True).encode()).hexdigest()[:16]
out = install / 'usr/share/bslap/backend.json'
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(manifest, indent=2) + '\n')
