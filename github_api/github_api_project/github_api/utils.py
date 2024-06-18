import requests
from datetime import datetime

def fetch_github_repositories():
    url = 'https://api.github.com/search/repositories'
    params = {
        'q': 'topic:django',  # Example: Fetch repositories related to Django
        'sort': 'stars',      # Sort by stars
        'order': 'desc',      # Sort in descending order
        'per_page': 100       # Number of results per page
    }

    headers = {
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()  # Raise an exception for bad responses

    return response.json()['items']
