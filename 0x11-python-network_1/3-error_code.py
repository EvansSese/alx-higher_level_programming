#!/usr/bin/python3
""" Script to display error code """


import urllib.request
import urllib.error
import sys


def display_error(url):
    """ Function to display error """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
    except urllib.error.URLError as e:
        print(f"Error sending request to URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    url = sys.argv[1]
    display_error(url)
