#!/usr/bin/python3
"""Module that defines the to_json_string function."""
import json


def to_json_string(my_obj):
    """Return the JSON representation (string) of an object."""
    return json.dumps(my_obj)
