#!/usr/bin/python3
from sys import argv
add = 0
if len(argv) <= 1:
    print(add)
else:
    for i in range(len(argv)):
        if i != 0:
            add += int(argv[i])
    print(add)
if __name__ == "__main__":
    argv
