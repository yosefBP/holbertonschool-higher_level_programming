#!/usr/bin/python3
"""Square with size"""


class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0):
        """Function constructor"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self. __size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size
