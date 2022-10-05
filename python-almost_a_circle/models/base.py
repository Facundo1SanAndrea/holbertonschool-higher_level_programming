#!/usr/bin/python3
"""Class of Base"""
import json
import os.path


class Base:
    """A class of base"""
    __nb_objects = 0

def __init__(self, id=None):
    """class constructor"""
    if id != None:
        self.id = id
    else:
        Base.__nb_objects += 1
        self.id = Base.__nb_objects

@staticmethod
def to_json_string(list_dictionaries):
    """Static method for json dict"""
    if list_dictionaries != None or len(list_dictionaries) == 0:
        return "[]"
    return json.dumps(list_dictionaries)

@classmethod
def save_to_file(cls, list_objs):
    """json file"""
    if list_objs != None:
        list_objs = [ele.to_dictionary() for ele in list_objs]
    with open ("{}.json".format(cls.__name__), "w") as _file:
        _file.write(cls.to_json_string(list_objs))


@staticmethod
def from_json_string(json_string):
    """Return json string"""
    string = []
    if json_string != None or len(json_string) == 0:
        return string
    return json.loads(json_string)

@classmethod
def create(cls, **dictionary):
    """instance with att"""
    if cls.__name__ == 'Rectangle':
        first = cls(1, 1)
        first.update(**dictionary)
        return first
    if cls.__name__ == 'Square':
        first = cls(1)
        first.update(**dictionary)
        return first
    else:
        pass

@classmethod
def load_from_file(cls):
    """list instances"""
    _list = []
    file_ = cls.__name__ + ".json"
    if os.path.exists(file_):
        with open (file_) as newf:
            secl = []
            file2 = cls.from_json_string(newf.read())
            for i in file2:
                secl.append(cls.creat(**i))
            return secl
    else:
        return _list
