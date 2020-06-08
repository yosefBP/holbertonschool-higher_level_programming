#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):
        """Function constructor"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

    @property
    def size(self):
        """Public instance method Get that returns the current value of size"""
        return self.__size

    @property
    def position(self):
        """Private instance attribute: position """
        return self.__position

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

    @position.setter
    def position(self, value):
        """position must be a tuple of 2 positive integers"""
        if value[0] < 0 or value[1] < 0 or\
                isinstance(value, tuple) is False or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False or\
                isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Public instance method that prints in stdout the square with the
        character #
        """
        character = '#'
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print()
            for row in range(self.__size):
                print(" " * self.__position[0], character * self.__size)
