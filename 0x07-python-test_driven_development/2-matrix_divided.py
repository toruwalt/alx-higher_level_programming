#!/usr/bin/python3
"""
    This function divides an entire matrix by a element div
    Raises:
    TypeError
"""


def matrix_divided(matrix, div):

    """
    Apple
    """

    x = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) != list:
        raise TypeError(x)
    for row in matrix:
        if type(row) != list:
            raise TypeError(x)
        for num in row:
            if type(num) != int and type(num) != float:

                raise TypeError(x)
    all_equal = all(len(row) == len(matrix[0]) for row in matrix)
    if all_equal is not True:
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        nums_A = []

        for i in matrix:
            nums_B = []
            for j in i:
                x = round((j / div), 2)
                nums_B.append(x)
            nums_A.append(nums_B)
        return nums_A
