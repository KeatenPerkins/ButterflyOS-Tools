import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import time
import unittest
from unittest.mock import patch
import zipfile

SOURCE = Path(__file__).resolve().parents[1] / 'overlay/projects/ROCKNIX/packages/misc/butterflyos-apps/sources/btools.py'
spec = importlib.util.spec_from_file_location('btools', SOURCE)
a = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a)

class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.key, self.public = self.root/'private.pem', self.root/'public.pem'
        subprocess.run(['openssl','genpkey','-algorithm','ED25519','-out',str(self.key)],check=True,capture_output=True)
        subprocess.run(['openssl','pkey','-in',str(self.key),'-pubout','-out',str(self.public)],check=True,capture_output=True)
        self.manager = a.Manager(self.root/'apps', {'api':1,'id':'rgds-plus','arch':'aarch64','features':['python3'],'layout':'dual'}, self.public)
        self.catalog_apps = []
        self.artifacts = {}
        self.fetch = patch.object(self.manager,'fetch',side_effect=self.download)
        self.fetch.start();self.addCleanup(self.fetch.stop)
        self.user_data = self.root/'bdex/collection.sqlite3'
        self.user_data.parent.mkdir();self.user_data.write_bytes(b'PRIVATE COLLECTION')

    def download(self, url, target, limit, expected=None):
        data = self.artifacts[url]
        target.write_bytes(data)
        a.require(len(data)<=limit,'size')
        a.require(expected is None or hashlib.sha256(data).hexdigest()==expected,'checksum')
        return len(data)

    def package(self, version='1.0.0', malicious=None):
        payload = b'import os\nprint(os.environ["BTOOLS_LAYOUT"])\n'
        manifest = dict(schema=1,id='bdex',version=version,api=1,platform='rgds-plus',kind='python',entry='bin/app.py',files={
            'bin/app.py':dict(sha256=hashlib.sha256(payload).hexdigest(),mode=0o755)})
        path=self.root/('bundle-'+version+'.zip')
        with zipfile.ZipFile(path,'w') as archive:
            archive.writestr('manifest.json',json.dumps(manifest))
            archive.writestr('bin/app.py',payload)
            if malicious:
                archive.writestr(malicious,b'ESCAPE')
        data=path.read_bytes();url='https://example.org/'+version+'.zip';self.artifacts[url]=data
        variant=dict(platforms=['rgds-plus'],architectures=['aarch64'],native=True,api=1,requires=['python3'],url=url,
                     sha256=hashlib.sha256(data).hexdigest(),size=len(data),unpacked_size=4096)
        self.catalog_apps=[dict(id='bdex',name='Bdex',version=version,variants=[variant])]
        return variant

    def sign(self, raw):
        data=self.root/'catalog-data';sig=self.root/'signature';data.write_bytes(raw)
        subprocess.run(['openssl','pkeyutl','-sign','-inkey',str(self.key),'-rawin','-in',str(data),'-out',str(sig)],check=True,capture_output=True)
        return sig.read_bytes()

    def catalog(self, sequence=1, expiry=None):
        raw=json.dumps(dict(schema=1,sequence=sequence,created=int(time.time())-1,expires=expiry or int(time.time())+3600,apps=self.catalog_apps)).encode()
        self.artifacts['https://example.org/catalog.json']=raw
        self.artifacts['https://example.org/catalog.json.sig']=self.sign(raw)
        self.manager.refresh('https://example.org/catalog.json')
        return raw

    def test_install_update_rollback_remove_preserves_collection(self):
        self.package();self.catalog();self.manager.install('bdex')
        first=self.manager.state()['apps']['bdex']['current']
        self.package('1.1.0');self.catalog(2);self.manager.install('bdex')
        self.assertEqual(self.manager.state()['apps']['bdex']['previous'],first)
        self.manager.change('bdex',True)
        self.assertEqual(self.manager.state()['apps']['bdex']['current'],first)
        self.manager.change('bdex')
        self.assertNotIn('bdex',self.manager.state()['apps'])
        self.assertEqual(self.user_data.read_bytes(),b'PRIVATE COLLECTION')

    def test_checksum_failure_and_interruption_keep_current(self):
        self.package();self.catalog();self.manager.install('bdex');before=self.manager.state()
        variant=self.package('1.1.0');self.catalog(2);before=self.manager.state()
        self.artifacts[variant['url']]=b'BROKEN'
        with self.assertRaises(a.AppError):self.manager.install('bdex')
        self.assertEqual(self.manager.state(),before)
        with patch.object(self.manager,'fetch',side_effect=OSError('disconnected')):
            with self.assertRaises(OSError):self.manager.install('bdex')
        self.assertEqual(self.manager.state(),before)

    def test_forged_catalog_and_replay_are_refused(self):
        self.package();raw=self.catalog(3)
        with self.assertRaises(a.AppError):self.manager.authenticate(raw+b' ',self.sign(raw))
        with self.assertRaises(a.AppError):self.catalog(2)
        self.assertEqual(self.manager.state()['sequence'],3)

    def test_catalog_icons_are_verified_before_use(self):
        self.package()
        image=b'example signed image'
        digest=hashlib.sha256(image).hexdigest()
        self.catalog_apps[0]['icon']=dict(url='https://example.org/icon.png',sha256=digest,size=len(image))
        self.artifacts['https://example.org/icon.png']=image
        self.catalog()
        self.assertEqual((self.manager.root/'catalog-icons'/(digest+'.png')).read_bytes(),image)
        self.catalog_apps[0]['icon']['sha256']='0'*64
        with self.assertRaises(a.AppError):self.catalog(2)
        self.assertEqual(self.manager.state()['sequence'],1)

    def test_expired_catalog_is_refused(self):
        self.package()
        with self.assertRaises(a.AppError):self.catalog(expiry=int(time.time())-1)

    def test_unknown_native_device_and_ambiguous_variants_are_refused(self):
        self.package();self.catalog();app=self.manager.catalog()['apps'][0]
        app['variants'][0]['platforms']=['future-device']
        with self.assertRaises(a.AppError):self.manager.variant(app)
        app['variants'][0]['platforms']=['*']
        with self.assertRaises(a.AppError):self.manager.variant(app)
        app['variants'][0]['native']=False
        self.manager.variant(app)
        app['variants'].append(dict(app['variants'][0]))
        with self.assertRaises(a.AppError):self.manager.variant(app)

    def test_archive_traversal_and_symlink_are_refused(self):
        for name in ['../escape','/absolute','bin/../../escape']:
            self.package(malicious=name);self.catalog()
            with self.assertRaises(a.AppError):self.manager.install('bdex')
            self.assertFalse((self.root/'escape').exists())
        variant=self.package();url=variant['url'];path=self.root/'symlink.zip'
        with zipfile.ZipFile(path,'w') as archive:
            info=zipfile.ZipInfo('manifest.json');info.external_attr=(0o120777)<<16
            archive.writestr(info,'/etc/shadow')
        self.artifacts[url]=path.read_bytes();variant.update(size=path.stat().st_size,sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        self.catalog()
        with self.assertRaises(a.AppError):self.manager.install('bdex')

    def test_running_app_lock_prevents_update(self):
        self.package();self.catalog();self.manager.install('bdex')
        with a.lock(self.manager.root/'locks/bdex.lock',shared=True):
            with self.assertRaises(a.AppError):self.manager.change('bdex')
            with self.assertRaises(a.AppError):self.manager.install('bdex')

    def test_reinstall_repairs_corruption_without_replacing_active_directory(self):
        self.package();self.catalog();self.manager.install('bdex');before=self.manager.state()['apps']['bdex']['current']
        old=self.manager.root/'store/bdex'/before['token'];(old/'bin/app.py').write_text('broken')
        self.manager.install('bdex');after=self.manager.state()['apps']['bdex']['current']
        self.assertNotEqual(before['token'],after['token'])
        self.assertEqual((old/'bin/app.py').read_text(),'broken')
        self.assertEqual(self.manager.state()['apps']['bdex']['previous'],before)

    def test_corrupt_previous_cannot_replace_current(self):
        self.package();self.catalog();self.manager.install('bdex')
        self.package('1.1.0');self.catalog(2);self.manager.install('bdex')
        before=self.manager.state()
        previous=before['apps']['bdex']['previous']
        (self.manager.root/'store/bdex'/previous['token']/'bin/app.py').write_text('bad')
        with self.assertRaises(a.AppError):self.manager.change('bdex',True)
        self.assertEqual(self.manager.state(),before)

    def test_tools_sync_preserves_other_tools_and_supports_optional_apps(self):
        tools=self.root/'tools';tools.mkdir()
        (tools/'gamelist.xml').write_text('<gameList><game><path>./Files.sh</path><name>Files</name></game></gameList>')
        self.manager.profile.update(tools_directory=str(tools),launcher_command='/storage/bin/btools')
        self.package();self.catalog();self.manager.install('bdex')
        self.assertTrue((tools/'Bdex.sh').is_file())
        self.assertIn('Files.sh',(tools/'gamelist.xml').read_text())
        self.manager.change('bdex')
        self.assertFalse((tools/'Bdex.sh').exists())
        self.assertIn('Files.sh',(tools/'gamelist.xml').read_text())

    def test_store_alias_cannot_redirect_cleanup_into_user_data(self):
        self.package();self.catalog()
        (self.manager.root/'store').symlink_to(self.user_data.parent, target_is_directory=True)
        with self.assertRaises(a.AppError):self.manager.install('bdex')
        self.assertEqual(self.user_data.read_bytes(),b'PRIVATE COLLECTION')

    def test_remove_bundled_tool_hides_it_and_reinstall_restores_it(self):
        tools=self.root/'tools';tools.mkdir()
        self.manager.profile.update(tools_directory=str(tools),bundled={'bdex':dict(command=['/bin/true'])})
        self.manager.sync('bdex')
        self.assertTrue((tools/'Bdex.sh').exists())
        self.manager.change('bdex')
        self.manager.sync('bdex')
        self.assertFalse((tools/'Bdex.sh').exists())
        self.assertIn('bdex',self.manager.state()['removed'])
        with self.assertRaises(a.AppError):self.manager.launch('bdex')
        self.assertEqual(self.manager.launch('bdex','web'),0)
        self.package();self.catalog();self.manager.install('bdex')
        self.assertTrue((tools/'Bdex.sh').exists())
        self.assertNotIn('bdex',self.manager.state()['removed'])
        self.assertEqual(self.user_data.read_bytes(),b'PRIVATE COLLECTION')

    def test_remove_only_deletes_its_own_launcher_and_metadata(self):
        tools=self.root/'tools';tools.mkdir()
        (tools/'Files.sh').write_text('KEEP')
        (tools/'gamelist.xml').write_text('<gameList><game><path>./Files.sh</path><name>Files</name></game></gameList>')
        self.manager.profile.update(tools_directory=str(tools))
        self.package();self.catalog();self.manager.install('bdex')
        self.assertIn('Bdex.sh',(tools/'gamelist.xml').read_text())
        self.manager.change('bdex')
        self.assertNotIn('Bdex.sh',(tools/'gamelist.xml').read_text())
        self.assertIn('Files.sh',(tools/'gamelist.xml').read_text())
        self.assertEqual((tools/'Files.sh').read_text(),'KEEP')

    def test_web_service_is_inactive_when_optional_app_was_never_installed(self):
        self.assertEqual(self.manager.launch('bdex','web'),0)
        with self.assertRaises(a.AppError):self.manager.launch('bdex')

    def test_invalid_state_path_is_rejected(self):
        a.atomic_json(self.manager.state_path,dict(schema=1,sequence=0,apps={'bdex':dict(current={'token':'../../elsewhere','version':'1.0.0'})}))
        with self.assertRaises(a.AppError):self.manager.state()

    def test_launch_is_offline_and_uses_profile_layout(self):
        self.package();self.catalog();self.manager.install('bdex')
        (self.manager.root/'catalog.json').unlink()
        with patch.object(a.subprocess,'run') as run:
            run.return_value.returncode=0
            self.assertEqual(self.manager.launch('bdex'),0)
            self.assertEqual(run.call_args.kwargs['env']['BTOOLS_LAYOUT'],'dual')

    def test_url_and_duplicate_metadata_guards(self):
        for url in ['http://example.org/a','file:///etc/shadow','https://user:pass@example.org/a']:
            with self.assertRaises(a.AppError):self.manager.url(url)
        with self.assertRaises(a.AppError):a.read_json('{"id":1,"id":2}')
        self.manager.local_test=True;self.manager.url('http://127.0.0.1:1234/a')
        with self.assertRaises(a.AppError):self.manager.url('http://192.168.1.2/a')

if __name__=='__main__':unittest.main()
