#!/usr/bin/python3
"""Count the subscribers of some redit"""
import requests
import sys


def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    response = requests.get(f"https://www.reddit.com/r/{subreddit}/about.json").json()
    r = response.get("data")
    return (r.get("subscribers"))


if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
