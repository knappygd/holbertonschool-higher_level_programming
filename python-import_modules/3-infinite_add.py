#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    res = 0
    argc = len(sys.argv) - 1

    for i in range(argc):
        res += int(sys.argv[i + 1])

    print("{}".format(res))
