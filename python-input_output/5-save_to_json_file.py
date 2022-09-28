#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """Save Object to a file"""
    with open(filename, 'w+') as file_open:
        file_open.write(json.dumps(my_obj))
