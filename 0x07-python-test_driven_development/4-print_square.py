#!/usr/bin/python3
""" Function to print square"""


def print_square(size):
    """
    Prints a square with the character '#' of the given size length.

    Args:
        size (int): The length of the square.

    Raises:
        TypeError: If size is not an integer or if it is a float less than 0.
        ValueError: If size is less than 0.

    Examples:
        >>> print_square(3)
        ###
        ###
        ###

        >>> print_square(5)
        #####
        #####
        #####
        #####
        #####

        >>> print_square(-2)
        Traceback (most recent call last):
        ...
        ValueError: size must be >= 0

        >>> print_square(2.5)
        Traceback (most recent call last):
        ...
        TypeError: size must be an integer

        >>> print_square("4")
        Traceback (most recent call last):
        ...
        TypeError: size must be an integer

    """

    if isinstance(size, int):
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            for _ in range(size):
                print("#" * size)
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    else:
        raise TypeError("size must be an integer")
