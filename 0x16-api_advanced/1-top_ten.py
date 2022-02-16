import requests


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/"
    path = f"r/{subreddit}/about.json"
    web = url + path
    print(web)
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/75.0.3770.100 Safari/537.36'
        }
    web_all = requests.get(web, headers=header, allow_redirects=False)
    if web_all.status_code >= 300:
        return 0
    return web_all.json().get('data').get('subscribers')
