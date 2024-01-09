#!/usr/bin/python3
"""Returns JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """PyObject to JSON"""
    return json.dumps(my_obj)
