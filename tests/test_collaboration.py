"""WDF 1.2 collaboration config and workflow smoke tests, stdlib only."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]

def load(path,name):
 spec=importlib.util.spec_from_file_location(name,ROOT/path)
 module=importlib.util.module_from_spec(spec)
 spec.loader.exec_module(module)
 return module

configure=load('scripts/configure_mode.py','configure_mode')
check=load('scripts/check_wdf.py','check_wdf_v12')

class CollaborationTests(unittest.TestCase):
 def test_modes_and_roundtrip(self):
  with tempfile.TemporaryDirectory() as td:
   root=Path(td);(root/'.wdf').mkdir()
   cfg={'schema_version':'1.2','mode':'solo','human_release_approval':True}
   (root/'.wdf/config.json').write_text(json.dumps(cfg))
   for mode in ('team','factory','solo'):
    configure.configure(mode,root)
    result=json.loads((root/'.wdf/config.json').read_text())
    self.assertEqual(result['mode'],mode)
    self.assertTrue(result['human_release_approval'])
 def test_mode_rejects_unknown(self):
  with self.assertRaises(ValueError):configure.configure('unrestricted',ROOT)
 def test_structure(self):
  self.assertEqual(check.validate(ROOT),[])
 def test_required_human_release_gate(self):
  with tempfile.TemporaryDirectory() as td:
   import shutil
   root=Path(td)
   shutil.copytree(ROOT,root,dirs_exist_ok=True)
   config_path=root/'.wdf/config.json'
   cfg=json.loads(config_path.read_text());cfg['human_release_approval']=False
   config_path.write_text(json.dumps(cfg))
   self.assertTrue(any('human_release_approval' in v for v in check.validate(root)))

if __name__=='__main__':unittest.main()
