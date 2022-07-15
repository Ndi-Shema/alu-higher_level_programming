#!/usr/bin/python3
def multiple_returns(sentence):
    a = len(sentence)
    b = []
    c = []
    d = []
    e = []
    x = []
    y = []
    if a == 0:
        b = list(sentence)
        b.append("None")
        b.append(a)

    else:
        c = list(sentence)
        d = c.append(sentence[0])
        e = c.append(a)
        x = (c, d)
        y = tuple(x)
        return x
