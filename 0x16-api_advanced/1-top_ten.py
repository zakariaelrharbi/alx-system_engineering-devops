#!/usr/bin/python3

"""
Importing requests module.
"""

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = requests.get(url, headers=user_agent, params=params)
    all_data = response.json()

    try:
        raw_data = all_data.get('data').get('children')

        for item in raw_data:
            print(item.get('data').get('title'))

    except Exception:
        print("None")
