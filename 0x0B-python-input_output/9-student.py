#!/usr/bin/python3
"""Returns a dict representation of students"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    """Retrieves a dictionary representation of a Student instance"""
    def to_json(self):
        return self.__dict__
