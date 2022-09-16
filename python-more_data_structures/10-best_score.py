#!/usr/bin/python3

from re import I


def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    Newvalue = 0
    NewSpaces = ""
    for i in a_dictionary.keys():
        if a_dictionary[i] > Newvalue:
            Newvalue = a_dictionary[i]
            NewSpaces = I

    return NewSpaces
