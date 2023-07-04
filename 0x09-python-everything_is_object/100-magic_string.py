#!/usr/bin/python3
def magic_string():
    magic_string.iterations = magic_string.iterations + 1 if hasattr(magic_string, 'iterations') else 1
    return ', '.join(['BestSchool'] * magic_string.iterations)
