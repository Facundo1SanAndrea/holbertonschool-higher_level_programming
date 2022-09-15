#!/usr/bin/python3


from xml.dom.minidom import Element


def search_replace(my_list, search, replace):
    if my_list is None:
        return

    new_list = [replace if element == search else element for element in my_list]
    return new_list
