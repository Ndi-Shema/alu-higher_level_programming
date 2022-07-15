#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    b = []
    y = []
    if a < 1:
        b.append("None")
        b.append(a)

    else:
        b.append(sentence[0])
        b.append(a)
        y = tuple(b)
        return y
