#!/usr/bin/python3
"""Module defines matrix_divided function."""


def matrix_divided(matrix, div):
    """Devide all elements of @matrix with div.

    Args:
        matrix (list): 2D list of integers
        div (int): Divider of elements of @matrix

    Returns:
        new divided matrix
    """
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    matrix_size = len(matrix[0])

    for one_D_List in matrix:
        new_one_D_List = []
        if len(one_D_List) != matrix_size:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in one_D_List:
            if isinstance(elem, int) or isinstance(elem, float):
                new_one_D_List.append(round(elem / div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
        new_matrix.append(new_one_D_List)

    return new_matrix
