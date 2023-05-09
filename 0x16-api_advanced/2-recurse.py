#!/usr/bin/python3
"""Recursive function to return top posts from a subreddit"""

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing the titles
     top posts
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=50".format(subreddit)
    headers = {"User-Agent": "My Client"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            hot_list.append(post['data']['title'])

        url = '{}&after={}'.format(url, posts['data']['after'])
        return hot_list
    else:
        return None
