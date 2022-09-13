#!/usr/bin/python3


def no_c(my_string):
    newstring = ""
    i = 0
    for i in my_string:
        if i != 'C' and i != 'c':
            newstring += i

    return newstring
