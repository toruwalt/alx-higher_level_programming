#!/usr/bin/python3

"""Define the class called Square"""


class Square:

    """A property(method turned attribute) of sizealso functions as a getter"""
    @property
    def size(self):
        return self.__size

    """A size attribute setter that checks if value is an integer and is greater than 0, then sets the size to the value"""
    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """It has a private instance attribute of size"""
    def __init__(self, size=0):                           self.__size = size

    """Public Instance method which returns the current square area"""
    def area(self):

        sizes = self.__size
        areaX = sizes * sizes
        return areaX
