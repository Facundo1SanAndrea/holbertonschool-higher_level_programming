#!/usr/bin/python3
"""a class Rectangle that defines a rectangle"""


from tkinter.messagebox import RETRY


class Rectangle:
    """Class of the rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                space_string += str(self.print_symbol) * self.width
                if i != self.height - 1:
                    space_string += "\n"
        return space_string

    def __repr__(self):
        """return a string representation of the rectangle"""
        return (f"Rectangle({self.width}, {self.height})")

    def __del__(self):
        """Print the message Bye rectangle."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
