#!/usr/bin/python3
"""function that returns True if the object is exactly an instance"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance"""
    return issubclass(a_class, type(obj))
