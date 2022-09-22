#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of these characters: ., ? and :"""


def text_indentation(text):
    """prints text"""
    if type(text) != str:
        raise TypeError("text must be a string")
    dot = False
    for letter in text:
        if dot:
            if letter == " ":
                continue
            dot = False
        print(f"{letter}", end='')
        if letter == '.' or letter == '?' or letter == ':':
            print('\n')
            dot = True
