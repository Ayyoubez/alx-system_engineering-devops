#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers

    Args:
        subreddit (str): The subreddit to query.
    Returns:
        int: The number of subscribers for the subreddit, or 0
    """
    res = requests.get(
        "https://www.reddit.com/r/{subreddit}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"},
    )

    if res.status_code == 200:
        return res.json().get("data").get("subscribers")
    else:
        return 0
