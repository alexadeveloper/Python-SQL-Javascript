#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [10, 20, 30],
    [40, 50, "Holberton"]
]
print(matrix_divided(matrix, 2))
print(matrix)
