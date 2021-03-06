#!/usr/bin/python3
"""
function that queries the Reddit API and
returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    get data of numbers of subscriptor
    """
    if subreddit is None:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    moz = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64)'
    app = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    chro = 'Chrome/75.0.3770.100 Safari/537.36'
    agen = moz + ' ' + app + ' ' + chro
    header = {'User-Agent': agen}

    web_all = requests.get(url, headers=header, allow_redirects=False)
    if web_all.status_code >= 300:
        return (0)
    return (web_all.json().get('data').get('subscribers'))
