#!/usr/bin/python3
from sys import argv
if len(argv) <= 1:
    print("0 arguments.")
else:
    print("{:d} arguments:".format(len(argv) - 1) if len(argv) > 2
          else "{} argument:".format(len(argv) - 1))
    for i in range(len(argv)):
        if i > 0:
            print("{:d}: {}".format(i, argv[i]))
if __name__ == "__main__":
    argv
