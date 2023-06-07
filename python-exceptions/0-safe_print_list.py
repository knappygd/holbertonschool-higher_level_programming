#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    ret = 0
    for i in range(x):
        try:
            ret += 1
            print("{}".format(my_list[i]), end="")
        except IndexError:
            break
    print()
    return ret
