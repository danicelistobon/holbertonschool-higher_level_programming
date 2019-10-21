#!/usr/bin/python3
"""Module to inherit from Rectangle
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of the Square class
            Args:
                size (int): square size
                x (int): attribute
                y (int): attribute
                id (int): unique id
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """Size getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """Size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>
        """
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,
                                                 self.width)
