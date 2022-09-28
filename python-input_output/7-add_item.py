#!/usr/bin/python3
"""script that adds all arguments to list, and then save them to a file"""

import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"
list_obj = []

if os.path.exists(filename):
    list_obj = load_from_json_file(filename)

for element in args:
    list_obj.append(element)
save_to_json_file(list_obj, filename)
