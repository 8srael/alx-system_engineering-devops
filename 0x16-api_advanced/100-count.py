#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, after="", counter={}, ini=0):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        after (str): The parameter for the next page of the API results.
        counter (int): The parameter of results matched thus far.
    """
    if ini == 0:
        for word in word_list:
            counter[word] = 0

    url = "https://api.reddit.com/r/{}/hot?after={}".format(subreddit, after)
    headers = {"User-Agent": "Python3"}
    response = request("GET", url, headers=headers).json()
    try:
        top = response['data']['children']
        _after = response['data']['after']
        for item in top:
            for word in counter:
                counter[word] += item['data']['title'].lower(
                    ).split(' ').count(word.lower())
        if _after is not None:
            count_words(subreddit, word_list, _after, counter, 1)
        else:
            str = sorted(counter.items(), key=lambda kv: kv[1], reverse=True)
            for name, num in str:
                if num != 0:
                    print('{}: {}'.format(name, num))
    except Exception:
        return None
