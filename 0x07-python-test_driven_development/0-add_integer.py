#!/usr/bin/python3
""" Add Integer - Adds up 2 numbers

    Raises: TypeError: If parameter a or b is not int or float

    Returns: A int computation of parameter b and b"""


def add_integer(a, b=98):

    """
    A + B is returned
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
