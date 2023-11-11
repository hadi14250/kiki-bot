import requests
from requests.exceptions import RequestException
from pprint import pprint
import threading

twitterHandle = "ordinalHO"
twitterSession = "?t=jkhlbh&s=04"
url = "https://x.com/{}{}".format(twitterHandle, twitterSession)

# Structure payload.
payload = {
    "source": "universal",
    "url": "https://x.com/{}{}".format(twitterHandle, twitterSession),
    "render": "html",
}

# Get response.
try:
    profileResponse = requests.request(
        'POST',
        'https://realtime.oxylabs.io/v1/queries',
        auth=('hadi14250', '05590560352Hk200018'), #Your credentials go here
        json=payload,
    )
except requests.ConnectionError as e:
    print(f"An error occurred: {e}")
except RequestException as e:
    print(f"An error occurred: {e}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except requests.exceptions.SSLError as e:
    print(f"SSL/TLS handshake error: {e}")
except requests.exceptions.Timeout as e:
    print(f"Request timed out: {e}")

with open('webScraperProfile.html', 'wb') as f:
    f.write(profileResponse.content)


payload = {
    "source": "universal",
    "url": "https://twitter.com/billyrestey/status/1723108332591030474?t=jqnZFH3KytAI1zwsOJyU-A&s=19",
    "render": "html",
}

try:
    tweetResponse = requests.request(
        'POST',
        'https://realtime.oxylabs.io/v1/queries',
        auth=('hadi14250', '05590560352Hk200018'), #Your credentials go here
        json=payload,
    )
except requests.ConnectionError as e:
    print(f"An error occurred: {e}")
except RequestException as e:
    print(f"An error occurred: {e}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
except requests.exceptions.SSLError as e:
    print(f"SSL/TLS handshake error: {e}")
except requests.exceptions.Timeout as e:
    print(f"Request timed out: {e}")

with open('webScraperTweet.html', 'wb') as f:
    f.write(tweetResponse.content)