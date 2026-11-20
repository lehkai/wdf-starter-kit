"""Minimal tests for v1.1 local tooling (Python standard library)."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,ROOT/path)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 return module
new=load('new_feature','scripts/new_feature.py')
check=load('check_wdf','scripts/check_wdf.py')

class WdfTests(unittest.TestCase):
 def test_repo_structure(self):
  self.assertEqual(check.validate(ROOT),[])
 def test_feature_created_without_overwrite(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d);(root/'templates').mkdir()
   (root/'templates'/'feature-plan.md').write_text((ROOT/'templates'/'feature-plan.md').read_text())
   p=new.make_plan('F-123','sample-feature',root=root,today='2026-11-17')
   self.assertTrue(p.exists());self.assertIn('feature_id: "F-123"',p.read_text());self.assertIn('2026-11-17',p.read_text())
   with self.assertRaises(FileExistsError):new.make_plan('F-123','another-slug',root=root)
 def test_invalid_input(self):
  for fid,slug in [('ABC','valid'),('F-001','Bad Slug'),('F-1','valid'),('F-002','../escape')]:
   with self.assertRaises(ValueError):new.make_plan(fid,slug,root=ROOT)

if __name__=='__main__':unittest.main()
