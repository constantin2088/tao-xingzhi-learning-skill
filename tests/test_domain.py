import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from learning_evidence import classify
class DomainTests(unittest.TestCase):
 def test_support_is_not_mastery(self):self.assertEqual(classify(dict(completed=True,independent=False,transfer_success=False)),'supported_completion')
 def test_no_transfer(self):self.assertEqual(classify(dict(completed=True,independent=True,transfer_success=False)),'independent_same_task')
 def test_transfer(self):self.assertEqual(classify(dict(completed=True,independent=True,transfer_success=True)),'observed_transfer')
 def test_inconsistent(self):
  with self.assertRaises(ValueError):classify(dict(completed=False,independent=False,transfer_success=True))
 def test_unknown_not_false(self):
  with self.assertRaises(ValueError):classify(dict(completed=True,independent=True))
