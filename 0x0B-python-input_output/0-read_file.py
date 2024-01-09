#!/usr/bin/python3
"""Function that reads text"""


def read_file(filename=""):
    """Takes a read mode and prints the text"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end=(""))
