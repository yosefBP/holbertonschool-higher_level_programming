#!/usr/bin/python3
"""Number of lines"""


def number_of_lines(filename=""):
    """Function that returns the number of lines of a text file"""
    with open(filename, encoding="utf-8") as file:
        num_lines = file.readlines()
    return len(num_lines)
