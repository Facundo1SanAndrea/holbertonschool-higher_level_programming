#!/usr/bin/python3
"""class Student that defines a student """



class Student:
    """A clas that defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        list_ = {}
        self_dict = self.__dict__

        if attrs is None:
            return self_dict

        if type(attrs) is list:
            for i in attrs:
                if hasattr(self, i):
                    list_[i] = getattr(self, i)
            return list_

        def  reload_from_json(self, json):
            self.__dict__.update(json)
