#!/usr/bin/env python3
"""Sign a release catalog from package metadata; never uploads or changes repository visibility."""
import argparse
import json
from pathlib import Path
import subprocess
import time
import urllib.parse

parser = argparse.ArgumentParser()
parser.add_argument('--packages', type=Path, required=True)
parser.add_argument('--base-url', required=True)
parser.add_argument('--sequence', type=int, required=True)
parser.add_argument('--key', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--local-test', action='store_true')
args = parser.parse_args()
url = urllib.parse.urlsplit(args.base_url)
if url.username or url.password or not (url.scheme == 'https' or (args.local_test and url.scheme == 'http' and url.hostname == '127.0.0.1')):
    parser.error('Use a public HTTPS download location, or explicit loopback testing')
apps = {}
for metadata in sorted(args.packages.glob('*.metadata.json')):
    package = json.loads(metadata.read_text())
    ident, version, variant = package['id'], package['version'], package['variant']
    variant['url'] = args.base_url.rstrip('/') + '/' + package['filename']
    entry = apps.setdefault(ident, dict(id=ident, name=package['name'], version=version, variants=[]))
    if entry['version'] != version:
        parser.error('All device variants for an app must use the same version')
    entry['description'] = package.get('description', '')
    if package.get('icon'):
        icon = dict(package['icon'])
        icon['url'] = args.base_url.rstrip('/') + '/' + icon.pop('filename')
        entry['icon'] = icon
    entry['variants'].append(variant)
if not apps or args.sequence < 1:
    parser.error('A non-empty package directory and positive sequence are required')
now = int(time.time())
data = dict(schema=1, sequence=args.sequence, created=now, expires=now + 90*86400, apps=list(apps.values()))
args.output.parent.mkdir(parents=True, exist_ok=True)
args.output.write_text(json.dumps(data, sort_keys=True, separators=(',', ':')))
subprocess.run(['openssl', 'pkeyutl', '-sign', '-inkey', str(args.key), '-rawin', '-in', str(args.output), '-out', str(args.output)+'.sig'], check=True)
print('Signed catalog:', args.output)
