#!/usr/bin/python3
"""Count the subscribers of some redit"""
import requests
import sys


def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 9}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        r2 = response.json().get("data")
        for r in r2.get("children"):
            print(r.get("data").get("title"))
if __name__ == '__main__':

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        number_of_subscribers(sys.argv[1])
