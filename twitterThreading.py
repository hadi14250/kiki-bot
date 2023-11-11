import requests
import threading
from requests.exceptions import RequestException

def make_request(payload, flag):
    try:
        response = requests.request(
            'POST',
            'https://realtime.oxylabs.io/v1/queries',
            auth=('hadi14250', '05590560352Hk200018'), #Your credentials go here
            json=payload,
        )
        if (flag == 'p'):
            with open('webScraperProfile.html', 'wb') as f:
                f.write(response.content)
        else:
            with open('webScraperTweet.html', 'wb') as f:
                f.write(response.content)
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



twitterHandle = "ordinalHO"
twitterSession = "?t=jkhlbh&s=04"
url = "https://x.com/{}{}".format(twitterHandle, twitterSession)

profilePayload = {
    "source": "universal",
    "url": "https://x.com/{}{}".format(twitterHandle, twitterSession),
    "render": "html",
}

tweetPayload = {
    "source": "universal",
    "url": "https://twitter.com/billyrestey/status/1723108332591030474?t=jqnZFH3KytAI1zwsOJyU-A&s=19",
    "render": "html",
}

thread1 = threading.Thread(target=make_request, args=(profilePayload, 'p'))
thread2 = threading.Thread(target=make_request, args=(tweetPayload, 't'))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()
