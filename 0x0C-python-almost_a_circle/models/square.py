#!/usr/bin/python3
""" Module for the Square Object """
from models.rectangle import Rectangle


class Square(Rectangle):
    """  The class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the size of the square """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns value for attributes """
        if args is not None and len(args) != 0:
            attr_names = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attr_names[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        attribute = ["id", "x", "width", "y"]
        dict_sqr = {}
        for attr in attribute:
            if attr == "width":
                dict_sqr["size"] = getattr(self, attr)
            else:
                dict_sqr[attr] = getattr(self, attr)

        return dict_sqr

    def __str__(self):
        """ Return the string representation of Square """
        result = ("[Square] ({}) {}/{} - {}").\
            format(self.id, self.x, self.y, self.width)

        return result
