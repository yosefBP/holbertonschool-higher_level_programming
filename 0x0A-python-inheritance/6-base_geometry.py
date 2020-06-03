#!/usr/bin/python3
"""class BaseGeometry"""


class BaseGeometry:
    """class BaseGeometry contains an empty method that
    handles an exception"""

    def area(self):
        """Raises an Exception with a message"""
        message = "area() is not implemented"
        raise Exception(message)
