#!/usr/bin/python3
"""Module that defines the Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle based on BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a rectangle.

        Args:
            width: the width (positive integer).
            height: the height (positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
