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
<<<<<<< HEAD
        if attrs is None:
            attrs = ["first_name", "last_name", "age"]
        elif type(attrs) is not list:
            raise TypeError("attrs must be a list of strings")
        elif all(type(ele) is str for ele in attrs):
            return {i: getattr(self, attr) for i in attrs if hasattr(self, i)}
        return self.__dict__
