#!/usr/bin/python3

def print_last_digit(number):
    last = abs(number) % 10
    if number < 0:
        last *= -1
    print("{}".format(last))

print_last_digit(27)
