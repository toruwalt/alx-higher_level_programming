#!/usr/bin/python3
"""Returns the dict description with JSON serialization of an object"""
import json


def class_to_json(obj):
    """Returns JSON from Class"""
    return json.dumps(obj.__dict__)
