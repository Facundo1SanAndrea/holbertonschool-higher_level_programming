#!/usr/bin/python3


def common_elements(set_1, set_2):
    if set_1 is None or set_2 is None:
        return

    inter_list = list(set(set_1).intersection(set_2))
    return inter_list
