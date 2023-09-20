# tests.py

import unittest
from app import add

class TestApp(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add(-3, -5)
        self.assertEqual(result, -8)

    def test_add_mixed_numbers(self):
        result = add(3, -5)
        self.assertEqual(result, -2)

    def test_failing_test(self):
        # This test intentionally fails
        self.assertEqual(1, 2)

if __name__ == '__main__':
    unittest.main()
