#!/usr/bin/python3
"""A function that writes to file"""

def write_file(filename="", text=""):
    """Takes 2 parameters"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
