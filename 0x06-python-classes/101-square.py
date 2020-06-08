#!/usr/bin/python3
"""Print Square instance"""


class Square:
    """Private instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):
        """Function constructor"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Private instance attribute: position """
        return self.__position

    @position.setter
    def position(self, value):
        """position must be a tuple of 2 positive integers"""
        if isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False or\
                isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Public instance method that prints in stdout the square with the
        character #
        """
        char = '#'
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for row in range(self.__size):
                print("{}{}".format(' '*self.__position[0], char*self.__size))

    def __str__(self):
        """Return a Square instance should have the same
        behavior as my_print()
        """
        obj_square = ""
        if self.size == 0:
            return obj_square
        for i in range(self.__position[1]):
            obj_square += "\n"
        for j in range(self.size):
            obj_square += "{}{}".format(' '*self.__position[0], '#'*self.__size)
            if j != (self.size - 1):
                obj_square += "\n"
        return obj_square
