#!/usr/bin/python3
""" Scriot to display status """


import requests


def display_status(url):
    """ Function to display status """
    response = requests.get(url)
    data = response.text
    print("Body response:")
    print(f"\t- type: {type(data)}")
    print(f"\t- content: {data}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    display_status(url)
