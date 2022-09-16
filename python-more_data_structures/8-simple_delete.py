#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key) is None:
        return a_dictionary
    else:
        pop = a_dictionary
        pop.pop(key)
        return pop
