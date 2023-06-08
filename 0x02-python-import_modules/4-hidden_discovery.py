#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    mod_name = "hidden_4"
    mod = __import__(mod_name, fromlist=['*'])
    names = [name for name in dir(mod) if not name.startswith('__')]
    names.sort()
    for name in names:
        print(name)
