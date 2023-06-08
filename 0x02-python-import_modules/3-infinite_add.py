#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = sys.argv
    num_args = len(args) - 1
    args_total = 0
    if num_args > 0:
        for i in range(num_args):
            args_total += int(args[i + 1])
    print("{}".format(args_total))
