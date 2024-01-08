#!/usr/bin/python3
"""Checks exact object"""


def is_same_class(obj, a_class):
    """Return True or False"""
    if type(obj) == a_class:
        return True
    else:
        return False
