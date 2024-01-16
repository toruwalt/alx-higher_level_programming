#!/usr/bin/python3
"""The Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Inherits from Base Class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    @property
    def width(self):
        """Getter and Setter of width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Getter and setter of height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Getter and setter of x"""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Getter and setter of y"""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance."""
        return (self.__width * self.__height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        if self.__width and self.__height != 0:
            for i in range(0, self.__y):
                print("")
            for j in range(0, self.__height):
                for k in range(0, self.__x):
                    print(' ', end='')
                for m in range(0, self.__width):
                    print('#', end='')
                print("")
        else:
            print("")

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
            if len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value
