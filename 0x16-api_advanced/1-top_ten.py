#!/usr/bin/python3
"""function that queries the Reddit API and
prints the titles of the first 10 hot posts listed
"""
import requests


def top_ten(subreddit):
    """Print top 10 posts"""
    if subreddit is None:
        print("None")

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    moz = 'Mozilla/5.0 (Windows NT 6.2; Win64; x64)'
    app = 'AppleWebKit/537.36 (KHTML, like Gecko)'
    chro = 'Chrome/75.0.3770.100 Safari/537.36'
    agen = moz + ' ' + app + ' ' + chro
    header = {'User-Agent': agen}

    web_all = requests.get(url, headers=header, allow_redirects=False)
    if web_all.status_code == 200:
        info = web_all.json().get('data').get('children')
        for i in info[0:10]:
            dicc = i.get('data').get('title')
            print(dicc)
    else:
        print("None")
