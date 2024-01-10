#!/usr/bin/python3
"""Returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
"""
import json


def class_to_json(obj):
    """Returns JSON from Class"""
    return json.dumps(obj.__dict__)
