#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        my_list.sort(reverse=True)
        maxim = my_list[0]
        return maxim
    else:
        return None
