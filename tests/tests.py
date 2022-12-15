import unittest
from scripts.login import access

class TestAccess(unittest.TestCase):
    def test_access(self):
        actual = access()
        expected = "apple"
        self.assertEqual(actual, expected)