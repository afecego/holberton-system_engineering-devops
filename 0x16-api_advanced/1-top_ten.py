#!/usr/bin/python3
"""function that queries the Reddit API and
prints the titles of the first 10 hot posts listed
"""
import requests


def top_ten(subreddit):
    """Print top 10 posts"""
    if subreddit is None:
        return None
    dicc = {}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/75.0.3770.100 Safari/537.36'
        }

    web_all = requests.get(url, headers=header, allow_redirects=False)
    if web_all.status_code >= 300:
        return 0
    info = web_all.json().get('data').get('children')
    for i in info[0:10]:
        dicc = i.get('data').get('title')
        return (dicc)
