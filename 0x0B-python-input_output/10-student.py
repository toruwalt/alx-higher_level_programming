#!/usr/bin/python3
"""Returns a dict representation of students"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Retrieves a dictionary representation of a Student instance"""
    def to_json(self, attrs=None):
        if attrs is None:
            attrs = ["first_name", "last_name", "age"]
        elif type(attrs) != list:
            raise TypeError("attrs must be a list of strings")
        elif  all(type(ele) == str for ele in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
