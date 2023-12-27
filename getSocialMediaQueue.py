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

load_dotenv()
jwt_token = getBotJwtTokenEnv()
url = "http://localhost:3000/api/bot/social"

headers = {
    "Authorization": f"Bearer {jwt_token}",
    "Content-Type": "application/json",
}

def getSocialMediaQueue():
    try:
        response = requests.get(url, headers=headers)
        if (response.status_code == 200):
            social_data = response.json()
            return (social_data)
        else:
            response.raise_for_status()
            print(response.text)
            return(None)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return (None)

# ----------------> Functions <----------------

def create_thread(userAccount, payload, proxyUsername, proxyPassword):
    thread = threading.Thread(target=make_request,
				args=(userAccount, payload, proxyUsername, proxyPassword))
    return thread


def make_request(userAccount, payload, proxyUsername, proxyPassWord, retry_attempts=3, retry_delay=5):
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
            userAccount.formatHtmlResponse(response)

            break  # Successful request, exit the loop
        except (ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError, RequestException) as e:
            print(f"An error occurred: {e}")
            if attempt < retry_attempts - 1:
                print(f"Retry Number {attempt + 1} for {userAccount.scomUserName} in {retry_delay} seconds...")
                time.sleep(retry_delay)
            else:
                print(f"\033[91mMax retries reached. Request failed for {userAccount.scomUserName}\033[0m")


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

def runSocialMediaThreads(parsedSocialMediaAccounts, threads_per_batch):
    threads = []
    for user in parsedSocialMediaAccounts:
        socialMediaAccount = create_thread(
            user,
            {"source": "universal", "url": user.url, "render": "html"},
            proxyUsername,
            proxyPassword
        )
        threads.append(socialMediaAccount)

    while threads:
        run_threads(threads, threads_per_batch)

def validateBeforeSending(SocialMediaAccountsToDB):
    print("Dont forget to adad a function in parseFollowers() to validate the object before sending to db")

def parseFollowers(parsedSocialMediaAccounts):
    SocialMediaAccountsToDB = []
    for user in parsedSocialMediaAccounts:
        if (user.socialMediaType == "Instagram"):
            user.followers = getInstaFollowers(user.soupHtml)
        elif (user.socialMediaType == "TikTok"):
            user.followers = getTiktokFollowers(user.soupHtml, user.html)
        elif (user.socialMediaType == "X"):
            user.followers = extractTwitterUserInteractionCount(user.soupHtml, "followers")
        else:
            user.followers = 0
        if (user.followers is not None) and (int(user.followers) > 0):
            user.validated = True
        else:
            try:
                # adding this because incase followers are none db doesnt accept them
                user.followers = 0
                addInvalidUsersToExcelSheet(user)
            except:
                print("Couldn't add user(s) to excel sheet")

        SocialMediaAccountsToDB.append({
        "id": user.id,
        "valid": user.validated,
        "followers": user.followers
        })
        validateBeforeSending(SocialMediaAccountsToDB)
    return (SocialMediaAccountsToDB)

def sendSocialMediaToDB(SocialMediaAccountsToDB):
    response = requests.post(url, data=json.dumps(SocialMediaAccountsToDB), headers=headers)
    if (response.status_code == 200) or (response.status_code == 201):
        print("Users added successfully!")
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)
