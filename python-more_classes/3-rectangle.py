#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """Class of the rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """retirbe the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrives the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.height + self.width))

    def __str__(self):
        """retrive a new string to it"""
        space_string = ""
        if self.width != 0:
            for i in range(self.height):
                space_string += "#" * self.width
                if i != self.height - 1:
                    space_string += "\n"
        return space_string
