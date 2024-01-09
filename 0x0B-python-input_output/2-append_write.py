#!/usr/bin/python3
"""A function that appends text"""


def append_write(filename="", text=""):
    """Takes 2 arguments"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
