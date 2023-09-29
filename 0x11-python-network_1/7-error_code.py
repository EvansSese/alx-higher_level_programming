#!/usr/bin/python3
""" Script to show error """


import requests
import sys


def show_error(url):
    """ Function to show error """
    response = requests.get(url)
    status_code = response.status_code
    if status_code >= 400:
        print(f"Error code: {status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    show_error(url)
