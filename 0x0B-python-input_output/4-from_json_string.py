#!/usr/bin/python3
"""Returns a Python object represented by a JSON string"""
import json


def from_json_string(my_str):
    """Coverts JSON to PyObject"""
    return json.loads(my_str)
