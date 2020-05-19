#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return (0)
    try:
        for i in range(x):
            print("{}".format(str(my_list[i])), end="")
        print()
    except IndexError:
        print()
        return (i)
    return (i + 1)