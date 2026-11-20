#!/usr/bin/env python3
"""Build self-contained Btool archives from audited source and a staged device root."""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import shutil
import tempfile
import zipfile

REPO = Path(__file__).resolve().parents[2]
SOURCE = REPO / 'overlay/projects/ROCKNIX/packages/misc/butterflyos-pokemon'
ENTRIES = {'blink': 'butterflyos-save-trade-sdl.py', 'bdex': 'butterflyos-bdex-sdl.py', 'bslap': 'butterflyos-bslap.py'}


def build(app, version, platform, stage, destination):
    if app not in ENTRIES or not re.fullmatch(r'\d{1,9}\.\d{1,9}\.\d{1,9}', version):
        raise ValueError('Invalid app or version')
    if platform not in ('rgds-plus', 'miyoo-flip'):
        raise ValueError('Qualify a platform profile before creating native packages')
    with tempfile.TemporaryDirectory() as temporary:
        root = Path(temporary)
        binary = root / 'bin'
        binary.mkdir()
        paths = {}
        def copy(original, target):
            original = str(original)
            source = stage / original.lstrip('/')
            if not source.is_file():
                raise ValueError('Missing audited native file: ' + original)
            output = root / target
            output.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, output)
            paths[original] = target
        for path in sorted((SOURCE / 'sources').iterdir()):
            if path.suffix in ('.py', '.json'):
                shutil.copy2(path, binary / path.name)
                paths['/usr/bin/' + path.name] = 'bin/' + path.name
            elif path.name == 'bdex-web':
                shutil.copytree(path, binary / path.name)
            elif path.suffix in ('.sh', '.gptk', '.dialogrc'):
                target = root / 'share' / path.name
                target.parent.mkdir(exist_ok=True)
                shutil.copy2(path, target)
                paths['/usr/share/butterflyos/' + path.name] = 'share/' + path.name
        assets = root / 'assets'
        assets.mkdir()
        icon = {'blink': 'butterfly-link.png', 'bdex': 'bdex.png', 'bslap': 'bslap.png'}[app]
        shutil.copy2(SOURCE / 'sources/images' / icon, assets / 'icon.png')
        copy('/usr/bin/butterflyos-save-trade', 'bin/butterflyos-save-trade')
        if app == 'bslap':
            backend = json.loads((stage / 'usr/share/bslap/backend.json').read_text())
            for original, expected in backend['files'].items():
                source = stage / original.lstrip('/')
                if hashlib.sha256(source.read_bytes()).hexdigest() != expected:
                    raise ValueError('Native backend checksum mismatch: ' + original)
                copy(original, 'runtime/' + original.lstrip('/'))
            if backend.get('gb_library_path'):
                paths[backend['gb_library_path']] = 'runtime/' + backend['gb_library_path'].lstrip('/')
            paths['/usr/share/bslap/backend.json'] = 'runtime/backend.json'
            (root / 'runtime/backend.json').write_text(json.dumps(backend))
        class Relocate(ast.NodeTransformer):
            def visit_Constant(self, node):
                if isinstance(node.value, str) and (node.value in paths or node.value == '/usr/bin'):
                    return ast.copy_location(ast.Call(func=ast.Attribute(value=ast.Name(id='btools_paths', ctx=ast.Load()), attr='path', ctx=ast.Load()), args=[node], keywords=[]), node)
                return node
            def visit_Call(self, node):
                # Backend paths and dictionary keys must expand together.
                if (isinstance(node.func, ast.Attribute) and isinstance(node.func.value, ast.Name) and
                    node.func.value.id == 'json' and node.func.attr == 'loads' and len(node.args) == 1 and
                    isinstance(node.args[0], ast.Call) and isinstance(node.args[0].func, ast.Attribute) and
                    node.args[0].func.attr == 'read_text' and ast.unparse(node.args[0].func.value) in ('MANIFEST', 'dual.MANIFEST')):
                    return ast.copy_location(ast.Call(func=ast.Attribute(value=ast.Name(id='btools_paths', ctx=ast.Load()), attr='manifest', ctx=ast.Load()), args=[node.args[0].func.value], keywords=[]), node)
                return self.generic_visit(node)
        for path in binary.glob('*.py'):
            tree = Relocate().visit(ast.parse(path.read_text()))
            tree.body.insert(0, ast.Import(names=[ast.alias(name='btools_paths')]))
            # Preserve __future__ placement if a source later needs it.
            tree.body = [n for n in tree.body if isinstance(n, ast.ImportFrom) and n.module == '__future__'] + [n for n in tree.body if not (isinstance(n, ast.ImportFrom) and n.module == '__future__')]
            path.write_text('#!/usr/bin/python3\n' + ast.unparse(ast.fix_missing_locations(tree)) + '\n')
            path.chmod(0o755)
        (binary / 'btools-paths.json').write_text(json.dumps(paths))
        shutil.copy2(Path(__file__).with_name('btools_paths.py'), binary / 'btools_paths.py')
        shutil.copytree(SOURCE / 'licenses', root / 'licenses')
        files = {}
        for path in sorted(root.rglob('*')):
            if path.is_file():
                files[str(path.relative_to(root))] = {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(), 'mode': 0o755 if path.stat().st_mode & 0o111 else 0o644}
        manifest = dict(schema=1, id=app, version=version, name={'blink':'Blink','bdex':'Bdex','bslap':'Bslap'}[app], icon='assets/icon.png', kind='python', entry='bin/' + ENTRIES[app], platform=platform, api=1, files=files)
        if app == 'bdex':
            manifest['services'] = {'web': 'bin/butterflyos-bdex-web.py'}
        (root / 'manifest.json').write_text(json.dumps(manifest, sort_keys=True))
        destination.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(root.rglob('*')):
                if path.is_file():
                    info = zipfile.ZipInfo(str(path.relative_to(root)), date_time=(2026, 1, 1, 0, 0, 0))
                    info.external_attr = (0o100000 | (0o755 if path.stat().st_mode & 0o111 else 0o644)) << 16
                    archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
        return dict(platforms=[platform], architectures=['aarch64'], native=True, api=1,
                    requires=['python3', 'sdl2', 'rocknix-storage-v1'] + (['bslap-' + ('rgds' if platform == 'rgds-plus' else 'flip') + '-v1'] if app == 'bslap' else []),
                    sha256=hashlib.sha256(destination.read_bytes()).hexdigest(), size=destination.stat().st_size,
                    unpacked_size=sum(path.stat().st_size for path in root.rglob('*') if path.is_file()))

def release_package(app, version, platform, stage, output):
    variant = build(app, version, platform, stage, output)
    icon_file = output.with_suffix('.icon.png')
    source_icon = {'blink':'butterfly-link.png','bdex':'bdex.png','bslap':'bslap.png'}[app]
    shutil.copy2(SOURCE / 'sources/images' / source_icon, icon_file)
    description = {'blink':'Copy and trade Pokemon between saves, or replay gifts and events.', 'bdex':'Build your Pokemon collection, inspect stats, and browse it on the web.', 'bslap':'Trade and battle in-game with another nearby ButterflyOS handheld.'}[app]
    metadata = dict(description=description, icon=dict(filename=icon_file.name, sha256=hashlib.sha256(icon_file.read_bytes()).hexdigest(), size=icon_file.stat().st_size), id=app, name={'blink': 'Blink', 'bdex': 'Bdex', 'bslap': 'Bslap'}[app], version=version, filename=output.name, variant=variant)
    output.with_suffix('.metadata.json').write_text(json.dumps(metadata, indent=2) + '\n')
    return metadata


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('app', choices=ENTRIES)
    parser.add_argument('--version', required=True)
    parser.add_argument('--platform', required=True)
    parser.add_argument('--stage', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(release_package(args.app, args.version, args.platform, args.stage, args.output), indent=2))
