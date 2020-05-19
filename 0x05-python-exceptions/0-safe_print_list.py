#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print("{:}".format(str(my_list[i])), end="")
        print()
    except IndexError:
        return (i)
    return (i + 1)
