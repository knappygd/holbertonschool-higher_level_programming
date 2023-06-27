#!/usr/bin/python3
""" Class that defines a square. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Inits a square. """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def __str__(self):
        """ Return in format [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)
