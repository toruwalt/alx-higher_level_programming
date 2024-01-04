#!/usr/bin/python3
"""A class called Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    """Gets the width of the rectangle"""
    def width(self):
        return (self.__width)

    @width.setter
    """Sets the width of the rectangle"""
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    """Gets the height of the rectangle"""
    def height(self):
        return (self.__height)

    @height.setter
    """Sets the height of the rectangle"""
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
