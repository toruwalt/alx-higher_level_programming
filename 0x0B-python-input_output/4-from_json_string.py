#!/usr/bin/python3

import json
"""Returns a Python object represented by a JSON string"""


def from_json_string(my_str):
    """Coverts JSON to PyObject"""
    return json.loads(my_str)
