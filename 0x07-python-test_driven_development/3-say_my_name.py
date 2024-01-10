#!/usr/bin/python3

"""
    say_my_name:
        This function prints a simple text
        "My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Takes first_name & last_name as parameters
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("first_name must be a string")

    else:
        print("My name is {} {}".format(first_name, last_name))
