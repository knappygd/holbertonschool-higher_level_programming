#!/usr/bin/python3
""" Base of all classes. """
from models.base import Base


class Rectangle(Base):
    """
    Inits a Rectangle

    Args:
        width: The width of the rectangle
        height: The height of the rectangle
        x: The x pos of the rectangle
        y: The y pos of the rectangle
        id: The id of the rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle. """
        return self.__height * self.__width

    def display(self):
        """ Print the rectangle. """
        [print("") for h in range(self.y)]
        for i in range(self.__height):
            [print(" ", end="") for w in range(self.x)]
            for j in range(self.__width):
                print("#", end="")
            print("\n", end="")

    def __str__(self):
        """ Return in format [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                       self.y, self.width,
                                                       self.height)

    def update(self, *args, **kwargs):
        """ Add arguments from args. """
        if args is not None and len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i in len(args):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)
