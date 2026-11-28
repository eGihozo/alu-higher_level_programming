#!/usr/bin/python3
"""Unittests for the Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for Base."""

    def setUp(self):
        """Reset the id counter and remove json files."""
        Base._Base__nb_objects = 0
        self.clean()

    def tearDown(self):
        """Remove json files."""
        self.clean()

    def clean(self):
        """Delete the json files created by the tests."""
        for name in ["Base.json", "Rectangle.json", "Square.json"]:
            if os.path.exists(name):
                os.remove(name)

    def test_auto_ids(self):
        """Ids increase automatically."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

    def test_given_id(self):
        """A given id is used and does not move the counter."""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 1)

    def test_other_ids(self):
        """Any value can be given as id."""
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-5).id, -5)
        self.assertEqual(Base("abc").id, "abc")

    def test_to_json_string(self):
        """to_json_string with None, empty and data."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        s = Base.to_json_string([{"id": 1}])
        self.assertEqual(s, '[{"id": 1}]')
        self.assertIsInstance(s, str)

    def test_from_json_string(self):
        """from_json_string with None, empty and data."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])
        self.assertEqual(Base.from_json_string('[{"id": 89}]'),
                         [{"id": 89}])

    def test_json_round_trip(self):
        """A list survives to_json_string then from_json_string."""
        data = [{"id": 89, "width": 10}, {"id": 7, "width": 1}]
        s = Base.to_json_string(data)
        self.assertEqual(Base.from_json_string(s), data)

    def test_save_none(self):
        """save_to_file(None) writes an empty list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty(self):
        """save_to_file([]) writes an empty list."""
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_rectangles(self):
        """save_to_file writes the rectangles."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_squares(self):
        """save_to_file writes the squares in Square.json."""
        s1 = Square(5)
        Square.save_to_file([s1])
        with open("Square.json") as f:
            data = Base.from_json_string(f.read())
        self.assertEqual(data, [s1.to_dictionary()])

    def test_save_overwrites(self):
        """save_to_file overwrites an existing file."""
        Rectangle.save_to_file([Rectangle(1, 1), Rectangle(2, 2)])
        Rectangle.save_to_file([Rectangle(3, 3)])
        self.assertEqual(len(Rectangle.load_from_file()), 1)

    def test_create_rectangle(self):
        """create builds a Rectangle with the same attributes."""
        r1 = Rectangle(3, 5, 1)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsInstance(r2, Rectangle)
        self.assertIsNot(r1, r2)
        self.assertEqual(str(r1), str(r2))
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_create_square(self):
        """create builds a Square with the same attributes."""
        s1 = Square(3, 1, 2, 9)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsInstance(s2, Square)
        self.assertIsNot(s1, s2)
        self.assertEqual(str(s1), str(s2))

    def test_load_missing_file(self):
        """load_from_file returns an empty list if there is no file."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_rectangles(self):
        """load_from_file returns equal but different rectangles."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        out = Rectangle.load_from_file()
        self.assertEqual(len(out), 2)
        self.assertIsInstance(out[0], Rectangle)
        self.assertIsNot(out[0], r1)
        self.assertEqual(str(out[0]), str(r1))
        self.assertEqual(str(out[1]), str(r2))

    def test_load_squares(self):
        """load_from_file returns squares for Square."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        out = Square.load_from_file()
        self.assertEqual(len(out), 2)
        self.assertIsInstance(out[1], Square)
        self.assertEqual(str(out[1]), str(s2))

    def test_load_empty_file(self):
        """load_from_file on an empty list returns an empty list."""
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])


if __name__ == '__main__':
    unittest.main()
