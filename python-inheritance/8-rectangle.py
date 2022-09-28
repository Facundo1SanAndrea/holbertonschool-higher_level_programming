#!/usr/bin/python3
"""a class rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class of rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        __width = width
        self.integer_validator("height", height)
        __height = height
