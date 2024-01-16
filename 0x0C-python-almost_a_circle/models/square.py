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
        return f"[Square] ({self.id}) {self.x}/{self.y} {self.width}"
