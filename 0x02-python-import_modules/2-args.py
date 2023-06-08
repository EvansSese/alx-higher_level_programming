#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    num_args = len(args) - 1
    if num_args == 0:
        print("{} arguments.".format(num_args))
    elif num_args == 1:
        print("{} argument:".format(num_args))
        print("{}: {}".format(num_args, args[1]))
    else:
        print("{} arguments:".format(num_args))
        for idx in range(num_args):
            i = idx + 1
            print("{}: {}".format(i, args[i]))
