#!/usr/bin/python3
""" Student to JSON with filter """


class Student:
    """class Student that defines a student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Public method that retrieves a dictionary representation of
        a Student instance (same as 10-class_to_json.py)
        attrs is a list of strings
        """
        new_dic = {}
        if attrs is None:
            new_dic = self.__dict__
        else:
            for i in attrs:
                if i in self.__dict__:
                    new_dic[i] = self.__dict__[i]
        return new_dic
