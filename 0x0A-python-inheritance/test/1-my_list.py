#!/usr/bin/python3
"""A class that inherits from a list"""


class MyList(list):
    """A wonderful class"""
    def __init__(self):
        super().__init__()
    """Returns a sorted list"""
    def print_sorted(self):
        print(sorted(self))
