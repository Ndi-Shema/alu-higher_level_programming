#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    b = []
    d = []
    e = []
    x = []
    y = []
    if a < 1:
        b.append("None")
        b.append(a)

    else:
        d = b.append(sentence[0])
        e = b.append(a)
        x = (d, e)
        y = tuple(x)
        return y
