#!/usr/bin/python3
"""Read n lines"""


def read_lines(filename="", nb_lines=0):
    """function that reads n lines of a text file (UTF8)
    and prints it to stdout
    """
    with open(filename, encoding="utf-8") as file:
        num_lines = file.readlines()
        if nb_lines <= 0:
            for i in num_lines:
                print(i, end='')
        elif len(num_lines) > 0:
            for i in range(0, nb_lines):
                print(num_lines[i], end='')
