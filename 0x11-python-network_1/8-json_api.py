#!/usr/bin/python3
""" Script to search user """


import requests
import sys


def search_user(url, q):
    """ Function to search user """
    try:
        response = requests.post(url, data={'q': q})
        response.raise_for_status()
        try:
            data = response.json()
            if data:
                print(f"[{data['id']}] {data['name']}")
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
    except requests.exceptions.RequestException as e:
        print(f"Error sending POST request: {e}")
    except Exception as e:
        print(f"No result")


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(url, q)
