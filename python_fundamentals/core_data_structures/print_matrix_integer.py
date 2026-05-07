#!/usr/bin/env python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    Format: Integers separated by spaces, one row per line.
    """
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                # Last element in the row (no trailing space)
                print("{:d}".format(row[i]), end="")
            else:
                # Middle elements (with trailing space)
                print("{:d}".format(row[i]), end=" ")
        print()
