#!/usr/bin/python3
#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    def test_single_element(self):
        self.assertEqual(max_integer([5]), 5)
    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 2, 5, 4]), 5)
        self.assertEqual(max_integer([10, 8, 12, 6]), 12)
        self.assertEqual(max_integer([100, 200, 150]), 200)
    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -2, -5, -4]), -1)
        self.assertEqual(max_integer([-10, -8, -12, -6]), -6)
        self.assertEqual(max_integer([-100, -200, -150]), -100)
    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([10, -8, 12, -6]), 12)
        self.assertEqual(max_integer([-100, 200, -150]), 200)
    def test_duplicate_max_value(self):
        self.assertEqual(max_integer([1, 3, 5, 5, 2, 4]), 5)
        self.assertEqual(max_integer([10, 10, 8, 12, 6]), 12)
        self.assertEqual(max_integer([-100, -100, 200, -150]), 200)
    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([10.2, 8.6, 12.7, 6.4]), 12.7)
if __name__ == '__main__':
    unittest.main()
