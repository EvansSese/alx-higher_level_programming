#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2
    add_func = __import__('add_0', fromlist=["add"])
    res = add_func.add(a, b)
    print("{} + {} = {}".format(a, b, res))
