#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the function max_integer."""

    def test_ordered_list(self):
        """Ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max is the first element."""
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_in_middle(self):
        """Max is in the middle."""
        self.assertEqual(max_integer([1, 2, 99, 4, 5]), 99)

    def test_max_at_end(self):
        """Max is the last element."""
        self.assertEqual(max_integer([1, 2, 3, 40]), 40)

    def test_one_element(self):
        """List with one element."""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument uses the default empty list."""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Only negative numbers."""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_positive_and_negative(self):
        """Positive and negative numbers."""
        self.assertEqual(max_integer([-10, 0, 10, -3]), 10)

    def test_floats(self):
        """List of floats."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_int_and_float(self):
        """Integers and floats mixed."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_duplicates(self):
        """Duplicated max value."""
        self.assertEqual(max_integer([4, 4, 1, 4]), 4)

    def test_all_same(self):
        """All elements are equal."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_big_numbers(self):
        """Very big numbers."""
        self.assertEqual(max_integer([10 ** 20, 5, 10 ** 19]), 10 ** 20)

    def test_tuple(self):
        """A tuple works too."""
        self.assertEqual(max_integer((1, 5, 3)), 5)

    def test_list_of_strings(self):
        """List of strings."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_mixed_types(self):
        """Comparing a string and an integer raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "a", 3])

    def test_none_in_list(self):
        """None inside the list raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, None, 3])

    def test_none_argument(self):
        """None instead of a list raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_integer_argument(self):
        """An integer instead of a list raises TypeError."""
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == '__main__':
    unittest.main()
