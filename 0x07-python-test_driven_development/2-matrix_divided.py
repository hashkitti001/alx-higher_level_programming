#!/usr/bin/python3
"""Defines a program that divides all elements of a matrix"""
def matrix_divided(matrix, div):
    """A function that divides all elements of a matrix, matrix by a number, div"""
    for i in range(len(matrix)):
        for j in range(len(matrix)[i]):
            if not isinstance(matrix[i][j], int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
