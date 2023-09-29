#!/usr/bin/python3
""" Script to display header """


import urllib.request
import sys


def display_header(url):
    """ Function to display response header """
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        if x_request_id:
            print("{}".format(x_request_id))
        else:
            print("X-Request-Id header not found in the response.")


if __name__ == "__main__":
    url = sys.argv[1]
    display_header(url)
