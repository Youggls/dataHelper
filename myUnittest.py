import unittest
import random
from marker import marker
from marksplit import marksplit
class TestGeneral(unittest.TestCase):
  def test_mark(self):
    with self.assertRaises(FileNotFoundError):
      marker(*self.rdargs(4))
  def test_marksplit(self):
    with self.assertRaises(FileNotFoundError):
      marksplit(*self.rdargs(4))
  def rdargs(self,size):
    return [str(random.random())]*size
if __name__ == '__main__':
  unittest.main()
