#!/usr/bin.python3
def multiple_returns(sentence):
    if sentence == "":
        return (0, 0)
    return (len(sentence), sentence[0])
