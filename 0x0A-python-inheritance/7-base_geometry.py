#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry contains two methods Integer validator
        and other empty method that handles an exception"""

    def area(self):
        """Raises an Exception with a message"""
        message = "area() is not implemented"
        raise Exception(message)

    def integer_validator(self, name, value):
        """This method validates *value is not an integer:
            raise a TypeError; is less or equal to 0:
            raise a ValueError"""
        message1 = name + ' must be an integer'
        message2 = name + ' must be greater than 0'
        if type(value) != int:
            raise TypeError(message1)
        if value <= 0:
            raise ValueError(message2)
