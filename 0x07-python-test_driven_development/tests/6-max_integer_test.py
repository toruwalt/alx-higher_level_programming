#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_actual_integer(self):
        """List of integers"""
        a = [1, 2, 3, 4]
        self.assertEqual(max_integer(a), 4)

    def test_reversed_integer(self):
        """List of integers big to small"""
        b = [4, 3, 2, 1]
        self.assertEqual(max_integer(b), 4)

    def test_empty_list(self):
        """List that has  no item"""
        c = []
        self.assertEqual(max_integer(c), None)

    def test_no_list(self):
        """Nothing  is passed into the function"""
        self.assertEqual(max_integer(), None)

    def test_only_one(self):
        """Only one integer is in list"""
        d = [1]
        self.assertEqual(max_integer(d), 1)

    def test_float_and_integer(self):
        """List has float and integer"""
        e = [1, 1.2, 2, 2.4, 4]
        self.assertEqual(max_integer(e), 4)

    def test_negtive_integer(self):
        """List of negative integer"""
        f = [-1, -2, -3, -4]
        self.assertEqual(max_integer(f), -1)

    def test_strings(self):
        """List of the same integer value"""
        g = ["I", "am", "a", "happy", "guy"]
        self.assertEqual(max_integer(g), "happy")

    def test_string_and_integer(self):
        """List of the strings and integer"""
        with self.assertRaises(TypeError):
            h = ["I", "bought", 2, "laptops", "in", 2023]
            max_integer(h)

    def test_set_not_list(self):
        """Set is passed, not List"""
        with self.assertRaises(TypeError):
            i = {1, 2, 3, 4}
            max_integer(i)

    def test_float(self):
        """List is of float"""
        j = [2.4, 1.2, 4.8, 0.6]
        self.assertEqual(max_integer(j), 4.8)

    def test_string(self):
        """List is of one string"""
        k = ["String"]
        self.assertEqual(max_integer(k), "String")

    def test_same_string(self):
        """List of the same string"""
        l = ["Happy", "Happy", "Happy"]
        self.assertEqual(max_integer(l), "Happy")

    def test_same_length_of_string(self):
        """1st letter Highest ASCII (Z) wins"""
        m = ["Happy", "Water", "Music", "Banks", "Z"]
        self.assertEqual(max_integer(m), "Z")

    def test_list_of_list(self):
        """List of list"""
        n = [[1, 2, 3], [1, 2], [1]]
        self.assertEqual(max_integer(n), [1, 2, 3])


if __name__ == '__main__':

    unittest.main()
