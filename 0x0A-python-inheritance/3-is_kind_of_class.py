#!/usr/bin/python3
"""Checks instance of the object"""


def is_kind_of_class(obj, a_class):
    """Returns True or False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
