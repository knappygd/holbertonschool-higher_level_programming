#!/usr/bin/python3

for d in range(10):
    for u in range(d + 1, 10):
        if d == 8:
            print("{}{}".format(d, u))
            break
        print("{}{}, ".format(d, u), end="")
