#!/usr/bin/python3
"""Subscribers Query on a given reddit"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 404:
        return 0
    re = res.json().get("data")
    return re.get("subscribers")
