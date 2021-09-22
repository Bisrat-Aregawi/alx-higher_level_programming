#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    _list = []
    for list in matrix:
        for element in list:
            _list.append(element**2)
        new_matrix.append(_list)
        _list = []
    return new_matrix
