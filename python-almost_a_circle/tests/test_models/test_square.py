#!/usr/bin/python3
"""Unittests for the Square class."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for Square."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def shown(self, sq):
        """Return what display() prints."""
        with patch("sys.stdout", new_callable=io.StringIO) as out:
            sq.display()
        return out.getvalue()

    def test_inherits(self):
        """Square is a Rectangle and a Base."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_ids(self):
        """Ids are automatic or given."""
        self.assertEqual(Square(5).id, 1)
        self.assertEqual(Square(2, 2).id, 2)
        self.assertEqual(Square(1, 2, 3, 4).id, 4)

    def test_attributes(self):
        """width and height equal size."""
        s = Square(5, 1, 2)
        self.assertEqual((s.width, s.height, s.x, s.y), (5, 5, 1, 2))
        self.assertEqual(s.size, 5)

    def test_missing_size(self):
        """size is mandatory."""
        with self.assertRaises(TypeError):
            Square()

    def test_type_errors(self):
        """Wrong types raise the Rectangle messages."""
        with self.assertRaises(TypeError) as c:
            Square("1")
        self.assertEqual(str(c.exception), "width must be an integer")
        with self.assertRaises(TypeError) as c:
            Square(1, "2")
        self.assertEqual(str(c.exception), "x must be an integer")
        with self.assertRaises(TypeError) as c:
            Square(1, 2, "3")
        self.assertEqual(str(c.exception), "y must be an integer")
        for bad in [1.5, None, True, [1], {}, (1,)]:
            with self.subTest(bad=bad):
                with self.assertRaises(TypeError):
                    Square(bad)

    def test_value_errors(self):
        """Wrong values raise the Rectangle messages."""
        with self.assertRaises(ValueError) as c:
            Square(0)
        self.assertEqual(str(c.exception), "width must be > 0")
        with self.assertRaises(ValueError) as c:
            Square(-1)
        self.assertEqual(str(c.exception), "width must be > 0")
        with self.assertRaises(ValueError) as c:
            Square(1, -1)
        self.assertEqual(str(c.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as c:
            Square(1, 0, -1)
        self.assertEqual(str(c.exception), "y must be >= 0")

    def test_area(self):
        """area is size * size."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_str(self):
        """__str__ format."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2)), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (3) 1/3 - 3")

    def test_display(self):
        """display uses x and y."""
        self.assertEqual(self.shown(Square(2)), "##\n##\n")
        self.assertEqual(self.shown(Square(2, 2)), "  ##\n  ##\n")
        self.assertEqual(self.shown(Square(3, 1, 3)),
                         "\n\n\n ###\n ###\n ###\n")

    def test_size_setter(self):
        """size setter changes width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.size, s.width, s.height), (10, 10, 10))
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")

    def test_size_setter_errors(self):
        """size setter validates like width."""
        s = Square(5)
        with self.assertRaises(TypeError) as c:
            s.size = "9"
        self.assertEqual(str(c.exception), "width must be an integer")
        with self.assertRaises(ValueError) as c:
            s.size = 0
        self.assertEqual(str(c.exception), "width must be > 0")
        self.assertEqual(s.size, 5)

    def test_update_args(self):
        """update with no-keyword arguments."""
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """update with keyword arguments."""
        s = Square(5)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_update_args_beat_kwargs(self):
        """kwargs are skipped when args exist."""
        s = Square(5)
        s.update(3, size=50)
        self.assertEqual((s.id, s.size), (3, 5))

    def test_update_validates(self):
        """update uses the validation."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(1, "a")
        with self.assertRaises(ValueError):
            s.update(size=-1)

    def test_to_dictionary(self):
        """to_dictionary has id, size, x and y."""
        s = Square(10, 2, 1)
        self.assertEqual(s.to_dictionary(),
                         {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_dictionary_update(self):
        """A dictionary can be used with update."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)


if __name__ == '__main__':
    unittest.main()
