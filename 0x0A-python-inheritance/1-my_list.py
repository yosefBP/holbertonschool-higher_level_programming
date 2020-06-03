#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """class that inherits from list"""

    def print_sorted(self):
        """Public instance method that prints the list type int,
        sorted (ascending sort)"""
        print(sorted(self))
