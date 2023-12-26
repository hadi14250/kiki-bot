import requests
import time
import threading
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError
import glob
import os
from user import user, user_objects
from formatHtml import formatHtml
from getCredentials import getProxyUsername, getProxyPassword
from extractInstaPostData import extractInstaPostData
from extractInstaPostData import checkUserNamePresence
from testFunctions import printUserInfo, printHtml
from extractInstaProfileData import getInstaFollowers
from extractTiktokProfileData import getTiktokFollowers
from extractTiktokPostData import extractTiktokPostData
from extractTwitterProfileData import extractTwitterUserInteractionCount
from extractTweet import getTweet
from sequenceMatcher import get_similarity_percentage
from calculateTotalReward import calculateTotalReward

def deleteHtmlFiles():
    curentDir = os.getcwd()
    pattern = '{}/htmlFiles/*.html'.format(curentDir)
    print("removing files from {}/htmlFile/*.html".format(curentDir))

    # Get a list of all files matching the pattern
    html_files = glob.glob(pattern)

    # Remove each file
    for file in html_files:
        os.remove(file)

def create_thread(userSocialMeida, payload, filename, proxyUsername, proxyPassword):
    thread = threading.Thread(target=make_request,
				args=(userSocialMeida, payload, filename, proxyUsername, proxyPassword))
    return thread

def make_request(userSocialMeida, payload, filename, proxyUsername, proxyPassWord, retry_attempts=3, retry_delay=5):
    for attempt in range(retry_attempts):   
        try:
            response = requests.request(
                'POST',
                'https://realtime.oxylabs.io/v1/queries',
                auth=(proxyUsername, proxyPassWord),
                json=payload,
                timeout=120
            )
            response.raise_for_status()
            userSocialMeida.formatHtmlResponse(response)
            printHtml( userSocialMeida.html, filename, "htmlFiles")

            break  # Successful request, exit the loop
        except (ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError, RequestException) as e:
            print(f"An error occurred: {e}")
            if attempt < retry_attempts - 1:
                print(f"Retry Number {attempt + 1} for {filename} in {retry_delay} seconds...")
                time.sleep(retry_delay)
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
        time.sleep(0.3)
    for thread in threads_to_run:
        thread.join()
    print("\033[92mlast batch finished\033[0m")

# ---------------->starts here<----------------

deleteHtmlFiles()

userLimit = 5 # (1 user has 6 requests or 6 threads)
usersPerBatch = 50
originalPostContent = "🌟 Calling all adventurers! The quest to uncover SCOM's elusive dad, the one and only Reese (aka our dev's dad), is officially underway! 🚀 Join the expedition and be a part of the excitement as we unravel the mystery surrounding his whereabouts. 🕵️‍♂️ Your contribution could be the"

threads_per_batch = usersPerBatch * 6


# Credentials
proxyUsername = "hadi14250" #getProxyUsername()
proxyPassword = "!zwTTdq86wLj6FM" #getProxyPassword()

threads = []
for user in user_objects[:userLimit]:
    if (user.instaProfile) and (user.instaPost) and (user.instaProfile != "nan") and (user.instaPost != "nan") and (user.instaProfile.profileUrl) and (user.instaProfile.profileUrl != "nan") and (user.instaPost.postUrl) and (user.instaPost.postUrl != "nan"):
        instagramProfileThread = create_thread(
            user.instaProfile,
            {"source": "universal", "url": user.instaProfile.profileUrl, "render": "html"},
            'instagram_profile_{}.html'.format(user.fullName),
            proxyUsername,
            proxyPassword
        )
        threads.append(instagramProfileThread)
        instagramPostThread = create_thread(
            user.instaPost,
            {"source": "universal", "url": user.instaPost.postUrl, "render": "html"},
            'instagram_post_{}.html'.format(user.fullName),
            proxyUsername,
            proxyPassword
        )
        threads.append(instagramPostThread)

    if (user.tiktokProfile) and (user.tiktokPost) and (user.tiktokProfile != "nan") and (user.tiktokPost != "nan") and (user.tiktokProfile.profileUrl) and (user.tiktokProfile.profileUrl != "nan") and (user.tiktokPost.postUrl) and (user.tiktokPost.postUrl != "nan"):
        tiktokProfileThread = create_thread(
            user.tiktokProfile,
            {"source": "universal", "url": user.tiktokProfile.profileUrl, "render": "html"},
            'tiktok_profile_{}.html'.format(user.fullName),
            proxyUsername,
            proxyPassword
        )
        threads.append(tiktokProfileThread)
        tiktokPostThread = create_thread(
            user.tiktokPost,
            {"source": "universal", "url": user.tiktokPost.postUrl, "render": "html"},
            'tiktok_post_{}.html'.format(user.fullName),
            proxyUsername,
            proxyPassword
        )
        threads.append(tiktokPostThread)

    if (user.twitterProfile) and (user.tweet) and (user.twitterProfile != "nan") and (user.tweet != "nan") and (user.twitterProfile.profileUrl) and (user.twitterProfile.profileUrl != "nan") and (user.tweet.postUrl) and (user.tweet.postUrl != "nan"):
        twitterProfileThread = create_thread(
            user.twitterProfile,
            {"source": "universal", "url": user.twitterProfile.profileUrl, "render": "html"},
            'twitter_profile_{}.html'.format(user.fullName),
            proxyUsername,
            proxyPassword
        )
        threads.append(twitterProfileThread)

        twitterPostThread = create_thread(
            user.tweet,
            {"source": "universal", "url": user.tweet.postUrl, "render": "html"},
            'tweet_{}.html'.format(user.fullName),
            proxyUsername,
            proxyPassword
        )
        threads.append(twitterPostThread)


while threads:
    run_threads(threads, threads_per_batch)

user_data_list = []

for user in user_objects[:userLimit]:
    user.instaProfile.followers = getInstaFollowers(user.instaProfile.soupHtml)
    user.instaPost.excractedUserName = checkUserNamePresence(user.instaProfile.csvUserName, user.instaPost.html)
    user.instaPost.postText = extractInstaPostData(user.instaPost.html, user.instaPost.soupHtml, "content")

    user.tiktokProfile.followers = getTiktokFollowers(user.tiktokProfile.soupHtml, user.tiktokProfile.html)
    user.tiktokPost.excractedUserName = extractTiktokPostData(user.tiktokPost.soupHtml, "userName", user.tiktokProfile.csvUserName, user.tiktokPost.html)
    user.tiktokPost.postText = extractTiktokPostData(user.tiktokPost.soupHtml, "content", user.tiktokProfile.csvUserName, user.tiktokPost.html)

    user.twitterProfile.followers = extractTwitterUserInteractionCount(user.twitterProfile.soupHtml, "followers")
    user.tweet.postText = getTweet(user.tweet.soupHtml)

    user.instaPost.contentSimilarity = get_similarity_percentage(user.instaPost.postText, originalPostContent, "insta")
    user.tiktokPost.contentSimilarity = get_similarity_percentage(user.tiktokPost.postText, originalPostContent, "tiktok")
    user.tweet.contentSimilarity = get_similarity_percentage(user.tweet.postText, originalPostContent, "twitter")

    user.totalPayment = calculateTotalReward(user)
    # # Define reward conditions based on followers count
    # reward = user.instaProfile.followers % 2 == 0
    # reward_amount = user.instaProfile.followers / 100

    # # Create a dictionary for each user
    # user_data = {
    #     "scomuser": user.instaProfile.followers,
    #     "reward": reward,
    #     "rewardAmount": reward_amount
    # }

    # # Add the dictionary to the list
    # user_data_list.append(user_data)

	# user.instaPost.postLike = extractInstaPostData(user.instaPost.html, user.instaPost.soupHtml, "likeCount")
	# user.instaPost.postDate = extractInstaPostData(user.instaPost.html, user.instaPost.soupHtml, "postDate")
	# user.tiktokPost.postLike = extractTiktokPostData(user.tiktokPost.soupHtml, "likeCount", user.tiktokProfile.csvUserName)
	# user.tiktokPost.postDate = extractTiktokPostData(user.tiktokPost.soupHtml, "postDate", user.tiktokProfile.csvUserName)

    printUserInfo(user, "testing.log", "testingLogs")

# print(user_data_list)
