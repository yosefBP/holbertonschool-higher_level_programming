#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry contains two methods Integer validator
    and other empty method that handles an exception
    """

    def area(self):
        """Raises an Exception with a message"""
        message = 'area() is not implemented'
        raise Exception(message)

    def integer_validator(self, name, value):
        """Public instance method that validates value
        value is an integer, name is a string
        """
        message1 = name + ' must be an integer'
        message2 = name + ' must be greater than 0'
        if isinstance(value, int) is False:
            raise TypeError(message1)
        if value <= 0:
            raise ValueError(message2)
