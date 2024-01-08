#!/usr/bin/python3
"""A class called Rectangle"""


class Rectangle:
    """Represents a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a rectangle.

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        Rectangle.print_symbol = self.print_symbol

    def __str__(self):
        """defines a rectangle as a human-readable string."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rows = [''.join([str(self.print_symbol) for _ in range(self.width)])
                for _ in range(self.height)]
        return '\n'.join(rows)

    def __repr__(self):
        """defines a rectangle as a string for debugging"""
        i = "Rectangle({}, {})".format(self.__width, self.__height)
        return i

    def __del__(self):
        """defines when a rectangle is destroyed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and return the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Calculates and return the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        if rect_2.area() > rect_1.area():
            return rect_2
