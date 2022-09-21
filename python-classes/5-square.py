#!/usr/bin/python3
"""Square class"""


from ctypes import sizeof


class Square:
    """square class"""
    def __init__(self, size=0):
        """class that defines a squares by instance attributes size"""
        self.__size = size
    
    @property
    def size(self):
        """"initialization of the property"""
        return self.__size
    
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """getting area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print in stdout he square with the character #"""
        for i in range(self.__size):
            for i in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
