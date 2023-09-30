#!/usr/bin/python3
""" Script to list last 10 commits """


import requests
import sys


def last_commits(api_url):
    """ Function to list last 10 commits """
    response = requests.get(api_url)
    response.raise_for_status()
    commits = response.json()
    if not commits:
        print("No commits found in the repository.")
    else:
        for commit in commits[:10]:
            sha = commit.get("sha")
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    api_url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    last_commits(api_url)
