#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new = [0, 0]
    for i in range(len(tuple_a)):
        if i > 1:
            break
        new[i] += tuple_a[i]
    for i in range(len(tuple_b)):
        if i > 1:
            break
        new[i] += tuple_b[i]
    return (new[0], new[1])
