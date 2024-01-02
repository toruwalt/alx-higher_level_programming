#!/usr/bin/python3

"""
    print_square:
        This prints a square with the character #
        It takes size as a parameter
"""


def print_square(size):

    """
        Returns: The Square of the given size
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for i in range(0, size):
            for j in range(0, size):
                print("#", end="")
            print("")
