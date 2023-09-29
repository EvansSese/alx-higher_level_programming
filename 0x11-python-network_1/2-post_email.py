#!/usr/bin/python3
""" Script to post email """


import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """ Function to post email """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
