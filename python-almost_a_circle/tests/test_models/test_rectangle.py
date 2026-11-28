#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for Rectangle."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    def shown(self, rect):
        """Return what display() prints."""
        with patch("sys.stdout", new_callable=io.StringIO) as out:
            rect.display()
        return out.getvalue()

    def test_inherits_base(self):
        """Rectangle is a Base."""
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_ids(self):
        """Ids are automatic or given."""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_getters(self):
        """Getters return the values."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual((r.width, r.height, r.x, r.y), (1, 2, 3, 4))

    def test_defaults(self):
        """x and y default to 0."""
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_setters(self):
        """Setters change the values."""
        r = Rectangle(1, 2)
        r.width = 5
        r.height = 6
        r.x = 7
        r.y = 8
        self.assertEqual((r.width, r.height, r.x, r.y), (5, 6, 7, 8))

    def test_private_attributes(self):
        """Attributes are private."""
        r = Rectangle(1, 2)
        self.assertEqual(r._Rectangle__width, 1)
        self.assertFalse("width" in r.__dict__)

    def test_missing_arguments(self):
        """width and height are mandatory."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_type_errors_setters(self):
        """Non-integers raise TypeError in every setter."""
        for name in ["width", "height", "x", "y"]:
            for bad in ["1", 1.5, None, True, [1], {}, (1,), {1}]:
                with self.subTest(name=name, bad=bad):
                    r = Rectangle(1, 1)
                    with self.assertRaises(TypeError) as c:
                        setattr(r, name, bad)
                    msg = name + " must be an integer"
                    self.assertEqual(str(c.exception), msg)

    def test_type_errors_constructor(self):
        """Non-integers raise TypeError in the constructor."""
        with self.assertRaises(TypeError) as c:
            Rectangle("1", 2)
        self.assertEqual(str(c.exception), "width must be an integer")
        with self.assertRaises(TypeError) as c:
            Rectangle(10, "2")
        self.assertEqual(str(c.exception), "height must be an integer")
        with self.assertRaises(TypeError) as c:
            Rectangle(1, 2, "3")
        self.assertEqual(str(c.exception), "x must be an integer")
        with self.assertRaises(TypeError) as c:
            Rectangle(1, 2, 3, "4")
        self.assertEqual(str(c.exception), "y must be an integer")

    def test_value_errors_width_height(self):
        """width and height must be > 0."""
        for name in ["width", "height"]:
            for bad in [0, -1, -100]:
                with self.subTest(name=name, bad=bad):
                    r = Rectangle(1, 1)
                    with self.assertRaises(ValueError) as c:
                        setattr(r, name, bad)
                    self.assertEqual(str(c.exception),
                                     name + " must be > 0")

    def test_value_errors_x_y(self):
        """x and y must be >= 0."""
        for name in ["x", "y"]:
            with self.subTest(name=name):
                r = Rectangle(1, 1)
                with self.assertRaises(ValueError) as c:
                    setattr(r, name, -1)
                self.assertEqual(str(c.exception), name + " must be >= 0")

    def test_value_errors_constructor(self):
        """Constructor validates values."""
        with self.assertRaises(ValueError) as c:
            Rectangle(0, 2)
        self.assertEqual(str(c.exception), "width must be > 0")
        with self.assertRaises(ValueError) as c:
            Rectangle(2, -2)
        self.assertEqual(str(c.exception), "height must be > 0")
        with self.assertRaises(ValueError) as c:
            Rectangle(10, 2, -3)
        self.assertEqual(str(c.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as c:
            Rectangle(10, 2, 3, -1)
        self.assertEqual(str(c.exception), "y must be >= 0")

    def test_zero_x_y_allowed(self):
        """x and y can be 0."""
        r = Rectangle(1, 1, 0, 0)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_area(self):
        """area returns width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_display_no_offset(self):
        """display without x and y."""
        self.assertEqual(self.shown(Rectangle(2, 2)), "##\n##\n")
        self.assertEqual(self.shown(Rectangle(1, 3)), "#\n#\n#\n")

    def test_display_with_offset(self):
        """display with x and y."""
        self.assertEqual(self.shown(Rectangle(2, 3, 2, 2)),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(self.shown(Rectangle(3, 2, 1, 0)),
                         " ###\n ###\n")

    def test_str(self):
        """__str__ format."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """update with no-keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_extra_args(self):
        """Extra arguments are ignored."""
        r = Rectangle(1, 1)
        r.update(5, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(r), "[Rectangle] (5) 4/5 - 2/3")

    def test_update_kwargs(self):
        """update with keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_args_beat_kwargs(self):
        """kwargs are skipped when args exist."""
        r = Rectangle(1, 1)
        r.update(7, width=50)
        self.assertEqual((r.id, r.width), (7, 1))

    def test_update_unknown_key(self):
        """Unknown keys are ignored."""
        r = Rectangle(1, 1)
        r.update(color="red")
        self.assertFalse(hasattr(r, "color"))

    def test_update_validates(self):
        """update uses the validation."""
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.update(1, "a")
        with self.assertRaises(ValueError):
            r.update(width=-1)

    def test_to_dictionary(self):
        """to_dictionary has all the attributes."""
        r = Rectangle(10, 2, 1, 9)
        self.assertEqual(r.to_dictionary(),
                         {"id": 1, "width": 10, "height": 2,
                          "x": 1, "y": 9})
        self.assertIsInstance(r.to_dictionary(), dict)

    def test_dictionary_update(self):
        """A dictionary can be used with update."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)


if __name__ == '__main__':
    unittest.main()
