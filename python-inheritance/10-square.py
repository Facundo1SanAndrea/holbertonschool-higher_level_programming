#!/usr/bin/python3
"""a class rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class rectangle of teh basegeomtry"""

    def __init__(self, size):
        """a square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return super().__str__()

    def area(self):
        """area square"""

        return self.__size ** 2
