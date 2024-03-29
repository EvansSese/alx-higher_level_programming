#!/usr/bin/python3
""" Finds the peak of an array """


def find_peak(list_of_integers):
    """ Function to find peak of a list """
    size = len(list_of_integers)

    if size == 0:
        return None
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]

    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
