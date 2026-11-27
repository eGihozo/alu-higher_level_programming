#!/usr/bin/python3
"""Module that defines the Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square based on Rectangle."""

    def __init__(self, size):
        """Initialize a square.

        Args:
            size: the size of the side (positive integer).
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
