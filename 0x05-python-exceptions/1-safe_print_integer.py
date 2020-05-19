#!/usr/bin/python3
def safe_print_integer(value):
    if not value and value != 0:
        return (False)
    try:
        print("{:d}".format(value), end="")
        print()
    except ValueError:
        return (False)
    return (True)
