#!/usr/bin/python3
""" Script to display header """


import requests
import sys


def display_header(url):
    """ Function to display header """
    try:
        response = requests.get(url)
        response.raise_for_status()
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(f"{x_request_id}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    url = sys.argv[1]
    display_header(url)
