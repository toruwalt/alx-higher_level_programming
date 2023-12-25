#!/usr/bin/python3

"""Define a class called Square"""


class Square:

    """Property called size"""
    @property
    def size(self):
        return self.__size
    """The setter of the size property"""
    @size.setter
    def size(self, value):

        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """The initialization at instantiation of the Square Class"""
    def __init__(self, size=0):
        self.__size = size

    """Area of square of size passed"""
    def area(self):
        return self.__size * self.__size

    """Method that prints in stdout the square with the character #"""
    def my_print(self):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print('#', end='')
            print("")
