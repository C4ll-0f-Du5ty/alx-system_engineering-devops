#!/usr/bin/python3
"""Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit."""
from requests import get


def recurse(subreddit, hot_list=[]):
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"limit": 100}
    response = get(url, params=params, allow_redirects=False)
    if response.status_code == 200:
        r2 = response.json().get("data").get("children")
        for r in r2:
            hot_list.append(r.get("data").get("title"))
        return hot_list
    else:
        return None
