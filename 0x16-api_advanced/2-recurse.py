#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
"""
import re
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Print top 10 posts whit recursive
    """
    if subreddit is None:
        return ("None")

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    moz = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64)'
    app = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    chro = 'Chrome/75.0.3770.100 Safari/537.36'
    agen = moz + ' ' + app + ' ' + chro
    header = {'User-Agent': agen}
    payload = {'count': 0, 'after': after}

    web = requests.get(url, headers=header, params=payload,
                       allow_redirects=False)
    if web.status_code >= 300:
        return None
    else:
        all = web.json().get('data').get('after')
        info = web.json().get('data').get('children')
        for i in info:
            hot_list.append(i.get('data').get('title'))
        if all is not None:
            return (recurse(subreddit, hot_list, all))
        else:
            return (hot_list)
