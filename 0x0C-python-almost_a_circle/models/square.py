#!/usr/bin/python3
"""The class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Inheirts from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Ininitializes"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns string representation"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """Assigns attributes"""
        if args and len(args) != 0:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.id = args[0]
                self.width = args[1]
            if len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
            if len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.x = args[2]
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

        @property
        def size(self):
            """Get/set the size of the Square."""
            return self.width

        @size.setter
        def size(self, value):
            self.width = value
            self.height = value
