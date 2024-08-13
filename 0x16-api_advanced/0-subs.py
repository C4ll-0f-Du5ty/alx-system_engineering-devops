#!/usr/bin/python3
"""Count the subscribers of some redit"""
import requests


def number_of_subscribers(subreddit):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    response = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        allow_redirects=False)
    r2 = response.json()
    if response.status_code == 200:
        return (r2.get("data").get("subscribers"))
    else:
        return 0
