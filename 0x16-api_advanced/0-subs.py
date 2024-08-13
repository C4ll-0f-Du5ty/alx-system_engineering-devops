#!/usr/bin/python3
"""Count the subscribers of some redit"""
import requests


def number_of_subscribers(subreddit):
    """Write a function that queries the Reddit API and
    returns the number of subscribers (not active users,
    total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0."""

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
