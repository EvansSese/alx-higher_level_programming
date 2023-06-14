#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_int = set(my_list)
    result = 0
    for i in uniq_int:
        result += i
    return result
