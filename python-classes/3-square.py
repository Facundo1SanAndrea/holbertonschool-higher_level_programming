#!/usr/bin/python3
"""square class"""


class Square:
    """class that defines a square for private attribute instance size"""
    def __init__(self, size=0):
        """Init class"""
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Area of the square"""
        return (self.__size * self.__size)
