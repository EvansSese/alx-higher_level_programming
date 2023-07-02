#!/usr/bin/python3
"""Function to divide matrix"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and returns a new matrix.

    Args:
        matrix (list): A list of lists containing integers or floats.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list: A new matrix with elements divided by the given number, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats,
                   or if each row of the matrix does not have the same size,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> div = 2
        >>> matrix_divided(matrix, div)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0], [3.5, 4.0, 4.5]]

        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> div = 0
        >>> matrix_divided(matrix, div)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero

        >>> matrix = [[1, 2, 3], [4, 5], [7, 8, 9]]
        >>> div = 2
        >>> matrix_divided(matrix, div)
        Traceback (most recent call last):
        ...
        TypeError: Each row of the matrix must have the same size

        >>> matrix = 5
        >>> div = 2
        >>> matrix_divided(matrix, div)
        Traceback (most recent call last):
        ...
        TypeError: matrix must be a matrix (list of lists) of integers/floats

        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> div = "2"
        >>> matrix_divided(matrix, div)
        Traceback (most recent call last):
        ...
        TypeError: div must be a number

    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix) or \
            not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
