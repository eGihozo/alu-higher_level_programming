#!/usr/bin/python3
"""Module that prints a square with the character #.

This module defines the function print_square.
"""


def print_square(size):
    """Print a square with the character #.

    Args:
        size: the length of a side (an integer >= 0).
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
