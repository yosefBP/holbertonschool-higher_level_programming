#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_dig = number % 10; last_dig2 = number % -10
if number <= 0:
    if last_dig2 != 0:
        print("Last digit of {:d} is {:d} and is\
 less than 6 and not 0".format(number, last_dig2))
    if last_dig2 == 0:
        print("Last digit of {:d} is {:d} and is 0".format(number, last_dig2))
if number > 0:
    if last_dig > 5:
        print("Last digit of {:d} is {:d} and\
 is greater than 5".format(number, last_dig))
    elif last_dig < 6 and last_dig != 0:
        print("Last digit of {:d} is {:d} and is\
 less than 6 and not 0 ".format(number, last_dig))
    if last_dig == 0:
        print("Last digit of {:d} is {:d} and is 0".format(number, last_dig))
