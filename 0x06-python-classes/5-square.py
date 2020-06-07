#!/usr/bin/python3
"""Printing a square"""


class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0):
        """Function constructor"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Public instance method Get that returns the current value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Public instance method set that validate an change the current
        value of size
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Public instance method that prints in stdout the square with the
        character #
        """
        character = '#'
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                for column in range(self.__size):
                    print(character, end='')
                print()
