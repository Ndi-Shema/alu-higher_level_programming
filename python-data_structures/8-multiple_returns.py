#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    if a == 0:
        b = list(sentence)
        b.append("None")
        return b
    else:
        c = list(sentence)
        return c[0]
