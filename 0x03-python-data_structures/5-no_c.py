#!/usr/bin/python3
def no_c(my_string):
    list_aux = list(my_string)
    for i in list_aux:
        if i == 'C' or i == 'c':
            list_aux.remove(i)
    return "".join(list_aux)
