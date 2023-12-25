#!/usr/bin/python3

"""Define the class called Square"""


class Square:

    """It has a private instance attribute of size"""

    def __init__(self, size=0):

        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise valueError("size must be >= 0")
        else:
            self.__size = size

    """Public Instance method which returns the current square area"""
    def area(self):

        sizes = self.__size
        areaX = sizes * sizes
        return areaX
