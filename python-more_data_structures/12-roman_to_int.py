#!/usr/bin/python3

def roman_to_int(roman_string):

    num = 0
    roms = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    for i in range(len(roman_string)):
        if (i != len(roman_string) - 1) and (roms[roman_string[i]] < roms[roman_string[i + 1]]):
            num += roms[roman_string[i]] * -1
        else:
            num += roms[roman_string[i]]
    return num
