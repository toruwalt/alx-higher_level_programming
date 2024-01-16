#!/usr/bin/python3
"""The class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inheirts from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} {self.width}"
"""
    @property
    def size(self):
        #Defines the getter and setter of the size property
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value
        self.__height = value
"""
