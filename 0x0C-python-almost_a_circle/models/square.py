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
        print("[Square] {} {}/{} - {}".format(self.id,
            self.x, self.y, self.size))
