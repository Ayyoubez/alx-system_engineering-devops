import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The subreddit to query.
    
    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0

# Example usage
if __name__ == "__main__":
    subreddit = "programming"
    print(number_of_subscribers(subreddit))  # Output: 756024
    subreddit = "this_is_a_fake_subreddit"
    print(number_of_subscribers(subreddit))  # Output: 0
