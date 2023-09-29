#!/usr/bin/python3
""" Script to post email """


import requests
import sys


def post_email(url, email):
    """ Function to post an email """
    try:
        data = {'email': email}
        response = requests.post(url, data=data)
        response.raise_for_status()
        body = response.text
        print(body)
    except requests.exceptions.RequestException as e:
        print(f"Error sending POST request to URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
