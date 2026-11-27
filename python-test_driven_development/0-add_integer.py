#!/usr/bin/python3
"""Module that adds two integers.

This module defines the function add_integer.
Floats are cast to integers before the addition.
"""


def add_integer(a, b=98):
    """Add two integers.
    a and b must be integers or floats, floats are cast to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
