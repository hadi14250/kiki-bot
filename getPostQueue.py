import requests
import json
import time
import threading
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError
import glob
import os
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
from addInvalidUsersToExcelSheet import addInvalidUsersToExcelSheet
from dotenv import load_dotenv
from getCredentials import getBotJwtTokenEnv
from addInvalidUsersToExcelSheet import addInvalidPostsToExcelSheet, addValidPostsToExcelSheet, add_InValid_Followers_But_Valid_Posts_To_Excel_Sheet

load_dotenv()

jwt_token = getBotJwtTokenEnv()
url = "http://localhost:3000/api/bot/posts"

headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Content-Type": "application/json",
}

def getPostQueue():
    try:
        response = requests.get(url, headers=headers)
        if (response.status_code == 200):
            post_data = response.json()
            return (post_data)
        else:
            response.raise_for_status()
            print(response.text)
            return(None)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return (None)


# ----------------> Functions <----------------

def create_thread(post, payload, proxyUsername, proxyPassword):
    thread = threading.Thread(target=make_request,
				args=(post, payload, proxyUsername, proxyPassword))
    return thread


def make_request(post, payload, proxyUsername, proxyPassWord, retry_attempts=3, retry_delay=5):
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
            post.formatHtmlResponse(response)

            break  # Successful request, exit the loop
        except (ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError, RequestException) as e:
            print(f"An error occurred: {e}")
            if attempt < retry_attempts - 1:
                print(f"Retry Number {attempt + 1} for {post.scomUserName} in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print(f"\033[91mMax retries reached. Request failed for {post.scomUserName}\033[0m")


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



# Credentials
proxyUsername = getProxyUsername()
proxyPassword = getProxyPassword()

def runPostThreads(parsedPosts, threads_per_batch):
    threads = []
    for post in parsedPosts:
        socialMediaPost = create_thread(
            post,
            {"source": "universal", "url": post.url, "render": "html"},
            proxyUsername,
            proxyPassword
        )
        threads.append(socialMediaPost)

    while threads:
        run_threads(threads, threads_per_batch)


def calcPaymentFollowers(followers, contentSimilarity):
    print("Remember to change the followers back to 300")
    followers = int(followers) if followers else 0  # Convert to int if followers is not None
    contentSimilarity = int(contentSimilarity) if str(contentSimilarity).replace('.', '').isdigit() else 0  # Convert to int if contentSimilarity is a digit
    
    if (contentSimilarity < 85) or ((followers) and (followers < 0)):
        return (0)
    if (followers == None):
        return (0)
    if (followers >= 0) and (followers <= 1000):
        return (10)
    elif (followers >= 1000) and (followers <= 5000):
        return (25)
    elif (followers >= 5000) and (followers <= 10000):
        return (40)
    elif (followers >= 10000) and (followers <= 20000):
        return (75)
    elif (followers >= 20000) and (followers <= 50000):
        return (125)
    elif (followers >= 50000) and (followers <= 150000):
        return (175)
    elif (followers >= 150000) and (followers <= 250000):
        return (250)
    elif (followers >= 250000) and (followers <= 500000):
        return (500)
    elif (followers >= 500000) and (followers <= 100000000):
        return (0)
    return (0)


def calculateTotalPostsReward(post):
    if (checkUserNamePresence(post.scomUserName, post.postText) == None):
        totalPayment = 0
    else:
        totalPayment = calcPaymentFollowers(post.followers, post.contentSimilarity)
    return (totalPayment)

def parsePosts(parsedPosts, originalPostContent):
    posts = []
    for post in parsedPosts:
        if (post.socialMediaType == "Instagram"):
            post.postText = extractInstaPostData(post.html, post.soupHtml, "content")
            post.contentSimilarity = get_similarity_percentage(post.postText, originalPostContent, "insta")
            post.totalPayment = calculateTotalPostsReward(post)
        elif (post.socialMediaType == "TikTok"):
            post.postText = extractTiktokPostData(post.soupHtml, "content", post.socialMedia, post.html)
            post.contentSimilarity = get_similarity_percentage(post.postText, originalPostContent, "tiktok")
            post.totalPayment = calculateTotalPostsReward(post)

        elif (post.socialMediaType == "X"):
            post.postText = getTweet(post.soupHtml)
            post.contentSimilarity = get_similarity_percentage(post.postText, originalPostContent, "twitter")
            post.totalPayment = calculateTotalPostsReward(post)
        print("post Text: | ", post.postText, " | Content Similraity: ", post.contentSimilarity, " total payment: ", post.totalPayment)
        if (post.totalPayment > 0):
            post.validated = True
            try:
                addValidPostsToExcelSheet(post)
            except:
                print("Couldn't add user to excel sheet")

        elif  (post.followers is not None and post.followers < 0) and ((post.contentSimilarity is not None) and (post.contentSimilarity > 85)):
            try:
                add_InValid_Followers_But_Valid_Posts_To_Excel_Sheet(post)
            except:
                print("Couldn't add user to excel sheet")
        else:
            try:
                addInvalidPostsToExcelSheet(post)   
            except:
                print("Couldn't add user to excel sheet")
        posts.append({
        "id": post.id,
        "reward": post.validated,
        "rewardAmount": post.totalPayment
        })
    return (posts)

def sendPostsToDB(postsToDB):
    response = requests.post(url, data=json.dumps(postsToDB), headers=headers)
    if (response.status_code == 200) or (response.status_code == 201):
        print("Posts added successfully!")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)
