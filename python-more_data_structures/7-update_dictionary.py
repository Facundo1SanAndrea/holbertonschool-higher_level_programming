#!/usr/bin/python3


from tkinter import N


def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None or key is   None or value is None:
        return

    updated_dictonary = a_dictionary
    updated_dictonary.update({key: value})
    return updated_dictonary
