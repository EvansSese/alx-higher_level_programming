#!/usr/bin/python3
a = 1
b = 2
add_func = __import__('add_0')
res = add_func.add(a, b)
print("{} + {} = {}".format(a, b, res))
