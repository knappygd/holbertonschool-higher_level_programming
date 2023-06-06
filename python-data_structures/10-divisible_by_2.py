#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new = [0] * len(my_list)
    for i in my_list:
        if my_list[i] % 2 == 0:
            new[i] = True
        else:
            new[i] = False
    return new
