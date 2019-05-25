#!/usr/bin/python3
"""simple function"""


def matrix_divided(matrix, div):
    """Function divides the elements of a matrix
    Args:
        matrix (list): the matrix
        div (int/float): divide by this number
    Returns:
        new matrix
    """
    count = 0
    if matrix is None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of\
    integers/floats")
    if type(matrix) == set:
            raise TypeError("matrix must be a matrix (list of lists) of \
    integers/floats")
    if type(matrix) == tuple:
        raise TypeError("matrix must be a matrix (list of lists) of \
    integers/floats")
    for i in matrix:
        if len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of \
        integers/floats")
        if type(i) == tuple:
            raise TypeError("matrix must be a matrix (list of lists) of \
        integers/floats")
        if type(i) == set:
            raise TypeError("matrix must be a matrix (list of lists) of \
        integers/floats")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is int or type(div) is float:
        count = 1
    else:
        raise TypeError("div must be a number")

    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    for a in range(len(matrix)):
        for b in range(len(matrix[a])):
            if type(matrix[a][b]) is not int:
                if type(matrix[a][b]) is not float:
                	raise TypeError("matrix must be a matrix (list of lists) of\
                integers/floats")

    new = []
    for number in matrix:
        new.append(list(map(lambda x: round(x / div, 2), number)))
    return new
