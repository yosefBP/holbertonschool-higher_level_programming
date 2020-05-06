#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        aux = 1
        for j in i:
            print("{:d}".format(j), end="")
            if aux < len(i):
                print(" ", end="")
            aux += 1
        print("")
