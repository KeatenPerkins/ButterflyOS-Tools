#!/usr/bin/env python3
"""Prepare a reviewed, signed release directory and public source snapshot offline."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tarfile
import tempfile

import package

ROOT = package.REPO


def copy_tree(source, target):
    shutil.copytree(source, target, ignore=shutil.ignore_patterns('__pycache__', '*.pyc'), dirs_exist_ok=True)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def prepare(args):
    if not re.fullmatch(r'[A-Za-z0-9-]+/[A-Za-z0-9._-]+', args.repository):
        raise ValueError('Invalid repository name')
    if not re.fullmatch(r'[A-Za-z0-9._-]+', args.tag):
        raise ValueError('Invalid release tag')
    if args.output.exists():
        raise ValueError('Use a fresh output directory; existing release candidates are never overwritten')
    args.output.mkdir(parents=True)
    public, assets = args.output/'repository', args.output/'assets'
    public.mkdir();assets.mkdir()
    readme=(ROOT/'docs/btools-public/README.md').read_text().replace('KeatenPerkins/ButterflyOS-Tools',args.repository)
    (public/'README.md').write_text(readme)
    (public/'.gitignore').write_text('__pycache__/\n*.pyc\n/builds/\n/.config/\n*.img\n*.img.gz\n*.srm\n*.sav\n*.state*\n')
    for relative in [
        'misc/butterflyos-pokemon', 'misc/butterflyos-apps', 'misc/pksav',
        'emulators/bslap-backend', 'emulators/bslap-retroarch',
        'emulators/libretro/gpsp-bslap-lr', 'emulators/libretro/gambatte-bslap-lr',
    ]:
        path=Path('overlay/projects/ROCKNIX/packages')/relative
        copy_tree(ROOT/path,public/path)
    copy_tree(ROOT/'tools/btools',public/'tools/btools')
    copy_tree(ROOT/'tests',public/'tests')
    # Only retain tests whose inputs are part of this app repository.
    for path in (public/'tests').iterdir():
        if path.is_file() and not path.name.startswith(('btools-', 'pokemon-')):
            path.unlink()
    config_path=public/'overlay/projects/ROCKNIX/packages/misc/butterflyos-apps/config/config.json'
    config=json.loads(config_path.read_text())
    feed_url=f'https://github.com/{args.repository}/releases/latest/download/catalog.json'
    config['catalog_url']=feed_url
    config_path.write_text(json.dumps(config,indent=2)+'\n')
    generated=subprocess.check_output(['openssl','pkey','-in',str(args.key),'-pubout'])
    if generated != (config_path.parent/'catalog-public.pem').read_bytes():
        raise ValueError('Signing key does not match the public key installed by the OS')
    for app in package.ENTRIES:
        package.release_package(app,args.version,'rgds-plus',args.stage,assets/f'{app}-rgds-plus-{args.version}.zip')
    subprocess.run(['python3',str(ROOT/'tools/btools/catalog.py'),'--packages',str(assets),
                    '--base-url',f'https://github.com/{args.repository}/releases/download/{args.tag}',
                    '--sequence',str(args.sequence),'--key',str(args.key),'--output',str(assets/'catalog.json')],check=True)
    native=public/'native-build'
    native.mkdir()
    for name, source in [
        ('flip-retroarch',args.flip_source/'projects/ROCKNIX/packages/emulators/libretro/retroarch'),
        ('flip-ffmpeg',args.flip_source/'projects/ROCKNIX/packages/multimedia/ffmpeg'),
        ('flip-ffmpeg-base',args.flip_source/'packages/multimedia/ffmpeg'),
        ('sameboy-lr',ROOT/'source/rocknix/projects/ROCKNIX/packages/emulators/libretro/sameboy-lr'),
    ]:
        copy_tree(source,native/name)
    provenance={'schema':1,'version':args.version,'platform':'rgds-plus','os_source':{'url':'https://github.com/ROCKNIX/distribution','revision':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT/'source/rocknix',text=True).strip()},'upstream':[]}
    with tempfile.TemporaryDirectory(dir=args.output) as temporary:
        sources=Path(temporary)/'upstream'
        sources.mkdir()
        native_sources=[
            ROOT/'source/rocknix/sources/bslap-retroarch/bslap-retroarch-9e1c1e8ac897625ed75920019f4f62a173a4eedf.tar.gz',
            ROOT/'source/rocknix/sources/gpsp-bslap-lr/gpsp-bslap-lr-5819380c2ffb0900219d700a382ee68c464ebb99.tar.gz',
            ROOT/'source/rocknix/sources/gambatte-bslap-lr/gambatte-bslap-lr-466e8b174982b3fdb5a026f60efc51972d1576b0.tar.gz',
            ROOT/'source/rocknix/sources/sameboy-lr/sameboy-lr-aa158a889a48b538a0302873704a34577c8eb67d.tar.gz',
            ROOT/'source/rocknix/sources/pksav/pksav-master.tar.gz',
            args.flip_source/'sources/retroarch/retroarch-bdba046fa6766380bc2457532f38e589df769aaf.tar.gz',
            args.flip_source/'sources/ffmpeg/ffmpeg-7.1.1.tar.xz',
        ]
        for path in native_sources:
            expected=Path(str(path)+'.sha256').read_text().split()[0]
            actual=digest(path)
            if actual != expected:
                raise ValueError('Cached source checksum mismatch: '+path.name)
            shutil.copy2(path,sources/path.name)
            provenance['upstream'].append(dict(file=path.name,sha256=actual,url=Path(str(path)+'.url').read_text().strip()))
        baseline=sources/'ROCKNIX-build-system.tar.gz'
        subprocess.run(['git','archive','--format=tar.gz','--output',str(baseline.resolve()),'HEAD'],cwd=ROOT/'source/rocknix',check=True)
        provenance['upstream'].append(dict(file=baseline.name,sha256=digest(baseline),revision=provenance['os_source']['revision']))
        config_dir=native/'configurations';config_dir.mkdir()
        build_roots=[
            ('rgds-gba-retroarch',ROOT/'source/rocknix/build.ROCKNIX-RK3566.aarch64/build/bslap-retroarch-9e1c1e8ac897625ed75920019f4f62a173a4eedf',['config.h','config.mk']),
            ('flip-gb-retroarch',args.flip_source/'build.ROCKNIX-RK3566.aarch64/build/retroarch-bdba046fa6766380bc2457532f38e589df769aaf',['config.h','config.mk']),
            ('flip-ffmpeg',args.flip_source/'build.ROCKNIX-RK3566.aarch64/build/ffmpeg-7.1.1',['config.h','ffbuild/config.mak']),
        ]
        for name, directory, files in build_roots:
            for filename in files:
                target=config_dir/name/filename;target.parent.mkdir(parents=True,exist_ok=True)
                text=(directory/filename).read_text().replace(str(ROOT/'source/rocknix'),'/build/rocknix').replace(str(args.flip_source),'/build/flip')
                target.write_text(text)
        (native/'SOURCE_PROVENANCE.json').write_text(json.dumps(provenance,indent=2)+'\n')
        (native/'README.md').write_text('''# Native components

The corresponding-source release archive contains the pinned upstream tarballs
under `upstream/`. Their URLs and SHA-256 values are in SOURCE_PROVENANCE.json.
The repo overlay contains RG DS package recipes and patches. This folder also
contains the Flip GB frontend/FFmpeg recipes and generated configuration records.
Use the pinned ROCKNIX build system with the corresponding package overrides,
architecture/toolchain and configuration. The application package builder takes
an audited staging root of native output; it does not silently pick host binaries.

The RG DS app uses an AArch64 GBA frontend/core and an isolated qualified GB
frontend/core with private FFmpeg 7.1.1 libraries. The baseline OS libraries stay
unchanged. Their checksums and link profiles are retained in each app package.
These build configurations are records, with local build paths normalized.
Commercial game ROMs, player saves and signing keys are excluded.
''')
        source_archive=assets/f'btools-source-{args.version}.tar.gz'
        with tarfile.open(source_archive,'w:gz',compresslevel=1) as archive:
            archive.add(public,arcname=f'ButterflyOS-Tools-{args.version}',filter=tar_filter)
            archive.add(sources,arcname=f'ButterflyOS-Tools-{args.version}/upstream')
    (public/'RELEASE.md').write_text(f'''# {args.tag}

First shared Btools download feed, app version {args.version}, RG DS Plus.
Contains Blink, Bdex and Bslap as optional installations with their required
native helpers. The OS image remains a separate download.

Use Tools → Y Add Tools → Add Tools → Refresh Tools. Select an app to add it.
Installed apps can be updated, rolled back or removed while retaining user data.

Only the RG DS package variant is offered in this initial feed. Flip package
integration and downloaded-package link regression remain to be qualified.
''')
    sums=[]
    for path in sorted(assets.iterdir()):
        if path.name.endswith('.metadata.json'):
            continue
        sums.append(f'{digest(path)}  {path.name}\n')
    (assets/'SHA256SUMS').write_text(''.join(sums))
    plan=dict(repository=args.repository,visibility='public',tag=args.tag,version=args.version,sequence=args.sequence,
              catalog_url=feed_url,published=False,assets=[line.strip().split('  ')[1] for line in sums]+['SHA256SUMS'])
    (args.output/'release-plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    return plan


def tar_filter(info):
    info.uid=info.gid=0
    info.uname=info.gname='root'
    info.mtime=0
    return info


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--repository',required=True)
    parser.add_argument('--tag',required=True)
    parser.add_argument('--version',required=True)
    parser.add_argument('--sequence',required=True,type=int)
    parser.add_argument('--stage',type=Path,required=True)
    parser.add_argument('--key',type=Path,required=True)
    parser.add_argument('--flip-source',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    print(json.dumps(prepare(parser.parse_args()),indent=2))
