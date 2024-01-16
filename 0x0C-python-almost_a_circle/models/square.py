#!/usr/bin/python3
"""The class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inheirts from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id, size, size, x, y)
        self.size = size
        self.x = x
        self.y = y
        self.id = None

    def __str__(self):
        return f"[Square] {self.id} {self.x}/{self.y} {self.size})"

    @property
    def size(self):
        """Defines the getter and setter of the size property"""
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        self.__height = value

