#!/usr/bin/python3
"""Square class"""


class Square:
    """Class that defines a square with private insatance attribute of size"""
    def __init__(self, size=0):
        """Init class"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
