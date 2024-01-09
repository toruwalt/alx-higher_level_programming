#!/usr/bin/python3
"""Checks for inheritance"""


def inherits_from(obj, a_class):
    """Returns True or False"""
    x = type(obj)
    y = type(a_class)
    if issubclass(x, y):
        return True
