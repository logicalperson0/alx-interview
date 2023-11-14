#!/usr/bin/python3
"""
A module for solving a 2d matrix!
"""


def rotate_2d_matrix(matrix):
    """rotates a 2d matrix 90 degrees clockwise."""
    # tempo = matrix
    new_arr = []
    rev_arr = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix)):
            new_row.append(matrix[j][i])
        new_arr.append(new_row)

    for x in new_arr:
        x.reverse()
        rev_arr.append(x)  # can use: rev_arr.append(x[::-1])

    for j in range(len(matrix)):
        matrix[j] = rev_arr[j]
