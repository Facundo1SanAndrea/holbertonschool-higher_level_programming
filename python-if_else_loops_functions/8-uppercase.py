#!/usr/bin/python3
islower = __import__('7-islower').islower


def uppercase(str):
    closestring = ''
    for a in str:
        if islower(a) is True:
            closestring += (chr(ord(a) - 32))
        else:
            closestring += a
    print("{}".format(closestring))
