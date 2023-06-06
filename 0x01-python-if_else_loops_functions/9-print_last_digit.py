#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        l_digit = number % 10
    else:
        l_digit = ((-1 * number) % 10)
    print("{}".format(l_digit))
    return l_digit
