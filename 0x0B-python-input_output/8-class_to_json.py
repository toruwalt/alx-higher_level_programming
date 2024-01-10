#!/usr/bin/python3
"""Returns the dict description with JSON serialization of an object"""


def class_to_json(obj):
    """Returns JSON from Class"""
    return obj.__dict__
