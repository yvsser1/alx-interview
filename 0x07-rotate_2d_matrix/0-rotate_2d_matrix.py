#!/usr/bin/python3
"""Module for rotating a 2D matrix 90 degrees clockwise"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (List[List[int]]): Square matrix to be rotated

    The rotation is performed in two steps:
    1. Transpose the matrix (swap elements across the main diagonal)
    2. Reverse each row
    """
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            # Swap elements across the main diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
