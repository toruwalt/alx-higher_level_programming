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
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for num in row:
            if type(num) != int and type(num) != float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    all_equal = all(len(row) == len(matrix[0]) for row in matrix)
    if all_equal != True:
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
