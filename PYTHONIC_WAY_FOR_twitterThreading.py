import requests
import time
import threading
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError

def make_request(payload, flag, filename):
    try:
        response = requests.post(
            'https://realtime.oxylabs.io/v1/queries',
            auth=('hadi14250', '05590560352Hk200018'),
            json=payload,
        )
        response.raise_for_status()
        with open(filename, 'wb') as f:
            f.write(response.content)
    except (ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError, RequestException) as e:
        print(f"An error occurred: {e}")

def create_thread(payload, flag, filename):
    thread = threading.Thread(target=make_request, args=(payload, flag, filename))
    time.sleep(0.5)
    thread.start()
    return thread

twitterHandle = "ordinalHO"
twitterSession = "?t=jkhlbh&s=04"

threads = [
    create_thread(
        {"source": "universal", "url": f"https://x.com/{twitterHandle}{twitterSession}", "render": "html"},
        "twitterProfile", 'twitterProfile.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://twitter.com/billyrestey/status/1723108332591030474?t=jqnZFH3KytAI1zwsOJyU-A&s=19", "render": "html"},
        "tweet", 'tweet.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/pubity/", "render": "html"},
        "instagramProfile", 'instagramProfile.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.instagram.com/p/CzTWqUWLLvJ/", "render": "html"},
        "instagramPost", 'instagramPost.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi", "render": "html"},
        "tiktokProfile", 'tiktokProfile.html'
    ),
    create_thread(
        {"source": "universal", "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354", "render": "html"},
        "tiktokPost", 'tiktokPost.html'
    ),
]

# Wait for all threads to finish
for thread in threads:
    thread.join()
