#!/usr/bin/python3
"""Query for all posts on subredit"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res= requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if res.status_code == 404:
        return None

    re = res.json().get("data")
    after = re.get("after")
    count += re.get("dist")
    for c in re.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list