#!/usr/bin/python3
"""Square class"""


class Square:
    """Class square"""
    def __init__(self, size=0):
        """class that defines a private instance attribute size"""
        self.__size = size

    @property
    def size(self):
        """initializing setter and getting size"""
        return self.__size

    @size.setter
    def size(self, value):
        """using size and not change it value"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of the square"""
        return (self.__size * self.__size)
