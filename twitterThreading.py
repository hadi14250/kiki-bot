import requests
import time
import threading
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError
import glob
import os
from user import User, user_objects


def deleteHtmlFiles():
    curentDir = os.getcwd()
    pattern = '{}/htmlFiles/*.html'.format(curentDir)
    print("removing files from {}/htmlFile/*.html".format(curentDir))

    # Get a list of all files matching the pattern
    html_files = glob.glob(pattern)

    # Remove each file
    for file in html_files:
        os.remove(file)

def printHtml(content, filename, dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    filename = os.path.join(dirName, filename)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def create_thread(url, filename):
    thread = threading.Thread(target=make_request, args=(url, filename))
    return thread

def make_request(url, filename, retry_attempts=3, retry_delay=5):
	proxies = {
		'http': 'http://hadi14250:!SrJY8SUHSYp8nB@unblock.oxylabs.io:60000',
		'https': 'http://hadi14250:!SrJY8SUHSYp8nB@unblock.oxylabs.io:60000',
	}
	headers = {
    "X-Oxylabs-Render": "html"
	}
	for attempt in range(retry_attempts):   
		try:
			response = requests.get(
				url,
				verify=False,  # Ignore the certificate
				proxies=proxies,
				headers=headers,
			)
			response.raise_for_status()
			printHtml( response.text, filename, "htmlFiles")
			break  # Successful request, exit the loop
		except (ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError, RequestException) as e:
			print(f"\033[91mAn error occurred: {e}\033[0m")
			if attempt < retry_attempts - 1:
				print(f"\033[94mRetry Number {attempt + 1} for {filename} in {retry_delay} seconds...\033[0m")
				time.sleep(retry_delay)
				# make_request
			else:
				print(f"\033[91mMax retries reached. Request failed for {filename}\033[0m")


def run_threads(thread_queue, num_threads_to_run):
    threads_to_run = []

    # Pop the specified number of threads from the queue
    for _ in range(num_threads_to_run):
        if thread_queue:
            thread = thread_queue.pop(0)
            threads_to_run.append(thread)

    # Start and wait for the threads to finish
    print("\033[92mstarting a new batch\033[0m")
    for thread in threads_to_run:
        thread.start()
        time.sleep(1)
    for thread in threads_to_run:
        thread.join()
    print("\033[92mlast batch finished\033[0m")

# ---------------->starts here<----------------

deleteHtmlFiles()

userLimit = 100 # (1 user has 6 requests or 6 threads)
usersPerBatch = 20

threads_per_batch = usersPerBatch * 6


threads = []
for user in user_objects[:userLimit]:
    instagramProfileThread = create_thread(
        user.insta.profileUrl,
        'instagram_profile_{}.html'.format(user.fullName)
    )
    threads.append(instagramProfileThread)

    instagramPostThread = create_thread(
        user.insta.postUrl,
        'instagram_post_{}.html'.format(user.fullName)
    )
    threads.append(instagramPostThread)

    tiktokProfileThread = create_thread(
        user.tiktok.profileUrl,
        'tiktok_profile_{}.html'.format(user.fullName)
    )
    threads.append(tiktokProfileThread)

    tiktokPostThread = create_thread(
        user.tiktok.postUrl,
        'tiktok_post_{}.html'.format(user.fullName)
    )
    threads.append(tiktokPostThread)

    twitterProfileThread = create_thread(
        user.twitter.profileUrl,
        'twitter_profile_{}.html'.format(user.fullName)
    )
    threads.append(twitterProfileThread)

    twitterPostThread = create_thread(
        user.twitter.postUrl,
        'tweet_{}.html'.format(user.fullName)
    )
    threads.append(twitterPostThread)


while threads:
    run_threads(threads, threads_per_batch)
