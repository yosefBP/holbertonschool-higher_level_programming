#!/usr/bin/python3
""" Use __slots__ to prevent the dynamic creation of attributes """


class LockedClass:
    """ Class without __dict__ and locked attributes """
    __slots__ = "first_name"
