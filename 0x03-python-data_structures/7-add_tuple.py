#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a and tuple_b:
        x = len(tuple_a)
        y = len(tuple_b)
        if x > 1 and y > 1:
            new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        elif x < 2 and y < 2:
            new_tuple = (tuple_a[0] + tuple_b[0], 0)
        elif y < 2:
            new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + 0)
        elif x < 2:
            new_tuple = (tuple_b[0] + tuple_b[0], tuple_b[1] + 0)
    elif tuple_a:
        new_tuple = (tuple_a[0], tuple_a[1])
    elif tuple_b:
        new_tuple = (tuple_b[0], tuple_b[1])
    else:
        new_tuple = (0, 0)
    return new_tuple
