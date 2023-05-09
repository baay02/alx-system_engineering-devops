import requests

def count_words(subreddit, word_list, after=None, counts={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after} if after else {}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()["data"]["children"]
        for post in data:
            title = post["data"]["title"].lower()
            for word in word_list:
                word = word.lower()
                if f" {word} " in f" {title} ":
                    counts[word] = counts.get(word, 0) + 1
        after = response.json()["data"]["after"]
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for count in sorted_counts:
                print(f"{count[0]}: {count[1]}")
    else:
        print(None)
