#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
from sys import exit


def main():
    if len(argv) < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = ["+", "-", "*", "/"]
    a = int(argv[1])
    b = int(argv[3])
    ope = argv[2]
    if argv[2]:
        if ope == operator[0]:
            print("{} {} {} = {}".format(a, ope, b, add(a, b)))
        elif ope == operator[1]:
            print("{} {} {} = {}".format(a, ope, b, sub(a, b)))
        elif ope == operator[2]:
            print("{} {} {} = {}".format(a, ope, b, mul(a, b)))
        elif ope == operator[3]:
            print("{} {} {} = {}".format(a, ope, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    main()
