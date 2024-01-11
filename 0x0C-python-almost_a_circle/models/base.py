#!/usr/bin/python3
"""Manage id attribute in all your future/
classes and to avoid duplicating the same code"""


class Base:
    """The 'Base' of all other classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize an instance"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
