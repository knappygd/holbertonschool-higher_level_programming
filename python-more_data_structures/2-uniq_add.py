#!/usr/bin/python3

def uniq_add(my_list=[]):
    new = list(set(my_list))
    add = 0
    for i in range(len(new)):
        add += new[i]
    return add
