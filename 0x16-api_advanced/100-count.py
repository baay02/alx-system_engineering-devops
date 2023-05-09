#!/usr/bin/python3
import requests
import time
import re

def count_words(subreddit, word_list, word_counts=None):
    if word_counts is None:
        word_counts = {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-agent': 'My Agent'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        titles = [post['data']['title'] for post in data['data']['children']]
        for title in titles:
            words = title.split()
            for word in words:
                word = re.sub(r'[^\w\s]', '', word)
                word = word.lower()
                if word in word_list:
                    if word in word_counts:
                        word_counts[word] += 1
                    else:
                        word_counts[word] = 1
        if len(word_list) > 1:
            count_words(subreddit, word_list[1:], word_counts)
    elif response.status_code == 404:
        print(f"Subreddit '{subreddit}' not found.")
    else:
        print(f"An error occurred: {response.status_code}")
    return word_counts

subreddit = "python"
word_list = ["python", "programming", "code", "developer"]
word_counts = count_words(subreddit, word_list)
sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
for word, count in sorted_word_counts:
    print(f"{word}: {count}")
