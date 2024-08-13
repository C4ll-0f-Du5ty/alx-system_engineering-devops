#!/usr/bin/python3
"""Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit."""
from requests import get


def top_ten(subreddit):
    """Getting Top 10 Posts"""
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 9}
    response = get(url, params=params)
    if response.status_code == 200:
        r2 = response.json().get("data").get("children")
        for r in r2:
            print(r.get("data").get("title"))
    else:
        print("None")
