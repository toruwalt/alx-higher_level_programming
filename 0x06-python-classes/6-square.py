#!/usr/bin/python3
"""Defines a class"""
class Square:
    @property
    def size(self):
        self.__self = self

    """
    A setter of the private attribute size

    Args:

        value(int) - new value to be inputted

    Raises:

        TypeError: If value is not integer
        ValueError: Value must be greater than 0
    """

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        self.__position = position

    """
    A setter for the position property


    Args:

        Value(tuple) - The tuples used

    Raises:

        TypeError - Input must be a tuple of two items
    """
    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    """
    Initializes every instance

    Args:
        
        size(int) - The size of the square
        position(tuple) - A tuple
    """
    
    def __init__(self, size=0, position=(0,0)):


