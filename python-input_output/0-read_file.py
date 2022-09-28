#!/usr/bin/python3
"""function that reads a text file and prints it to stdout"""


def read_file(filename=""):
    """open a file and return stdout"""
    with open(filename, mode="r", encoding="utf-8") as file_read:
        print(file_read.read(), end="")
