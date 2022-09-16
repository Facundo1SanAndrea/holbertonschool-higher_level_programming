#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    Newvalue = 0
    NewSpaces = ""
    for key in a_dictionary.keys():
        if a_dictionary[key] > Newvalue:
            Newvalue = a_dictionary[key]
            NewSpaces = key

    return NewSpaces
