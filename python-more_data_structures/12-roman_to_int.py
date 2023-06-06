#!/usr/bin/python3

def roman_to_int(roman_string):

    num = 0

    nums = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(len(roman_string)):
        if roman_string[i] >= roman_string[i + 1]:
            num += nums[roman_string[i]]
        else:
            num += nums[roman_string[i + 1]] - nums[roman_string[i]]
    return num
