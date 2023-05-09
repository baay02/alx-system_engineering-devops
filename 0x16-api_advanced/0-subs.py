#!/usr/bin/python3

""" a script to retrieve the no of subs on a subreddi"""

import requests


def number_of_subscribers(subreddit):
    """return the no of subs on subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": 'My Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        no_subs = data.get("data").get("subscribers")
        return no_subs
    else:
        return 0
