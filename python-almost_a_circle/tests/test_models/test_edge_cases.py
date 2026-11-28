#!/usr/bin/python3
"""Extra edge case unittests for Rectangle and Square."""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestEdgeCases(unittest.TestCase):
    """Edge cases for the constructors."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def test_rectangle_width_zero(self):
        """Rectangle(0, 1) raises ValueError."""
        with self.assertRaises(ValueError) as c:
            Rectangle(0, 1)
        self.assertEqual(str(c.exception), "width must be > 0")

    def test_rectangle_height_zero(self):
        """Rectangle(1, 0) raises ValueError."""
        with self.assertRaises(ValueError) as c:
            Rectangle(1, 0)
        self.assertEqual(str(c.exception), "height must be > 0")

    def test_rectangle_both_zero(self):
        """Rectangle(0, 0) raises ValueError for the width first."""
        with self.assertRaises(ValueError) as c:
            Rectangle(0, 0)
        self.assertEqual(str(c.exception), "width must be > 0")

    def test_rectangle_negative(self):
        """Rectangle(-1, 1) and Rectangle(1, -1) raise ValueError."""
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)

    def test_rectangle_x_y_minus_one(self):
        """Rectangle(1, 1, -1) and Rectangle(1, 1, 0, -1) raise."""
        with self.assertRaises(ValueError) as c:
            Rectangle(1, 1, -1)
        self.assertEqual(str(c.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as c:
            Rectangle(1, 1, 0, -1)
        self.assertEqual(str(c.exception), "y must be >= 0")

    def test_rectangle_float_and_none(self):
        """Floats and None raise TypeError in the constructor."""
        with self.assertRaises(TypeError):
            Rectangle(1.5, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, None)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1.5)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, None)

    def test_rectangle_string_x_y(self):
        """Strings for x and y raise TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "a")
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, "a")

    def test_square_zero_and_negative(self):
        """Square(0) and Square(-1) raise ValueError."""
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-1)

    def test_square_x_y_minus_one(self):
        """Square(1, -1) and Square(1, 0, -1) raise ValueError."""
        with self.assertRaises(ValueError):
            Square(1, -1)
        with self.assertRaises(ValueError):
            Square(1, 0, -1)

    def test_square_float_and_none(self):
        """Floats and None raise TypeError for Square."""
        with self.assertRaises(TypeError):
            Square(1.5)
        with self.assertRaises(TypeError):
            Square(None)


if __name__ == '__main__':
    unittest.main()
