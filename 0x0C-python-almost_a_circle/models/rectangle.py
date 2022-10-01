#!/usr/bin/python3
""" rectangle.py """
from models.base import Base


class Rectangle(Base):
    """ The class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize the instances """

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """ Returns the width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the new for the width of the rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Returns the height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the new value for the height of rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Returns the x coordinates of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets the new for the x coordinates of the rectangle """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Returns the y coordinates of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets the new value for the y coordinates of rectangle """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints in stdout the Rectangle instance with the character '#' """
        for _ in range(self.__y):
            print()

        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if args is not None and len(args) != 0:
            attr_names = ["id", "width", "height", "x", "y"]

            for i in range(len(args)):
                setattr(self, attr_names[i], args[i])
        else:
            if kwargs is not None and len(kwargs) != 0:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle """
        dict_rect = {}
        attribute = ["x", "y", "id", "height", "width"]

        for attr in attribute:
            dict_rect[attr] = getattr(self, attr)

        return dict_rect

    def __str__(self):
        """ Return the string  represtation of rectangle """
        result = ("[Rectangle] ({}) {}/{} - {}/{}").\
            format(self.id, self.__x, self.__y, self.__width, self.__height)
        return result
