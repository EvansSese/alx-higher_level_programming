#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for item in my_list:
            print("{}".format(item), end="")
            i += 1
            if i == x:
                break
        print()
    except IndexError:
        return i
    return i
