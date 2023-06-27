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
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Add arguments from args and kwargs. """
        if args is not None and len(args) > 0:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def __str__(self):
        """ Return in format [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)
