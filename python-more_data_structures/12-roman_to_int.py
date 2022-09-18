#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return (0)
    reset = 0
    dictonary = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500,'M': 1000}
    time = ()
    for i in roman_string:
        if len(time) == 0:
            time = i
        for x in dictonary:
            if i == x:
                if dictonary[time] < dictonary[i]:
                    reset -= dictonary[time] * 2
                reset += dictonary[i]
                time = x
                break
    return (reset)
