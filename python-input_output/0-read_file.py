#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="utf8") as file:
        print(file.read(), end="")
