#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        count = 1
        size = len(matrix)
        for i in matrix:
            for j in i:
                if count == size:
                    print("{:d}".format(j), end='')
                else:
                    print("{:d}".format(j), end=' ')
                count += 1
            print()
            count = 1
    else:
        print()
