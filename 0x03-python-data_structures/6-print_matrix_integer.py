#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        aux1 = 0
        for j in i:
            aux = len(i)
            aux1 += 1
            print("{:d}".format(j), end="")
            if aux1 < aux:
                print(end=" ")
        print()
