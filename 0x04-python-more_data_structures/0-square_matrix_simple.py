#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sqr_matrix = []
    sqrs = []
    for i in matrix:
        for j in i:
            sqrs.append(j ** 2)
        sqr_matrix.append(sqrs)
        del sqrs
        sqrs = []
    return sqr_matrix
