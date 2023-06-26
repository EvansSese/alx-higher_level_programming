#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    try:
        for i in range(x):
            val = my_list[i]
            try:
                print("{:d}".format(val), end="")
                counter += 1
            except (ValueError, TypeError):
                pass
    except IndexError:
        pass
    print()
    return counter
