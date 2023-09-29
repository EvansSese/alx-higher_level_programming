#!/usr/bin/python3
""" Script to get status """


import urllib.request


url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(url) as res:
            data = res.read()
            print("Body response:")
            print("    - type: {}".format(type(data)))
            print("    - content: {}".format(data))
            print("    - utf8 content: {}".format(data.decode('utf-8')))
    except urllib.error.URLError as e:
        print(f"Error fetching URL: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
