#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ""):
        return (0, "None")
    first = sentence[:1]
    Length = len(sentence)
    newTuple = (Length, first)
    return newTuple
