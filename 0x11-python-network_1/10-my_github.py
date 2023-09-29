#!/usr/bin/python3
""" Function to fetch githib users """


import requests
import sys


def show_github_id(username, pat):
    """ Function to get user id """
    api_url = "https://api.github.com/user"
    auth = (username, pat)
    response = requests.get(api_url, auth=auth)
    user_data = response.json()
    user_id = user_data.get("id")
    if user_id:
        print(f"{user_id}")
    else:
        print(None)


if __name__ == "__main__":
    username = sys.argv[1]
    pat = sys.argv[2]
    show_github_id(username, pat)
