#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-2, -1, 0, 1, 2, 3]), 3)
#        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer())



if __name__ == "__main__":
    unittest.main()
