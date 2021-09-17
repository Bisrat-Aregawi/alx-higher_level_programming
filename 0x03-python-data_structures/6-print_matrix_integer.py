#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for list in matrix:
            for element in list:
                if element == list[len(list) - 1]:
                    print("{:d}".format(element), end="")
                elif len(list) > 1:
                    print("{:d}".format(element), end=" ")
                else:
                    print("{:d}".format(element), end="")
            print()
