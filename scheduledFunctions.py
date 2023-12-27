from parseSocialMediaGetRequest import parseSocialMediaGetRequest
from getSocialMediaQueue import getSocialMediaQueue, runSocialMediaThreads, parseFollowers, sendSocialMediaToDB
from getPostQueue import  getPostQueue, runPostThreads, parsePosts, sendPostsToDB
from parsePostsGetRequest import parsePostsGetRequest
from time import sleep
from getCredentials import getAdminJwtTokenEnv
from dotenv import load_dotenv
import requests
import json

load_dotenv()

campaigneBody = {
    "order": "ASC",
    "page": 1,
    "take": 10
}

campaigneUrl = "http://localhost:3000/api/campaign/paginate/true"

def sendPostReqCampaignPaginate():
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(campaigneUrl, data=json.dumps(campaigneBody), headers=headers)
    if response.status_code in [200, 201]:
        data = response.json().get("data", [])
        for item in data:
            content = item.get("content", "")
        return (content)
    else:
        print(f"Failed to retreive campaign content with status code: {response.status_code}")
        print(response.text)
        return (None)


originalPostContent = "🌟 Calling all adventurers! The quest to uncover SCOM's elusive dad, the one and only Reese (aka our dev's dad), is officially underway! 🚀 Join the expedition and be a part of the excitement as we unravel the mystery surrounding his whereabouts. 🕵️‍♂️ Your contribution could be the"
threads_per_batch = 250

# # ---------> Social Media get request and then parse to a json object (SocialMediaAccountsToDB) that will be sent to queue <----------
def runSocialMediaScheduler():
    socialMediaResponseJson = getSocialMediaQueue()
    if (socialMediaResponseJson != None):
        print("someone signed up")
        parsedSocialMediaAccounts = parseSocialMediaGetRequest(socialMediaResponseJson)
        runSocialMediaThreads(parsedSocialMediaAccounts, threads_per_batch)
        SocialMediaAccountsToDB = parseFollowers(parsedSocialMediaAccounts)
        print(SocialMediaAccountsToDB)
        sendSocialMediaToDB(SocialMediaAccountsToDB)

    else:
        print("No New Sign Ups Yet, trying again in 30 mins")
# -----------------------------


# # ---------> Posts get request and then parse to a json object (postsToDB) that will be sent to queue <----------
def runPostScheduler():
    # originalPostContent = sendPostReqCampaignPaginate()
    # if (originalPostContent == None):
    #     return
    # print("Campaigne Content: ", originalPostContent)
    # sleep (5)
    postResponseJson = getPostQueue()
    if (postResponseJson != None):
        print("Someone Applied for a reward")
        parsedPosts = parsePostsGetRequest(postResponseJson)
        runPostThreads(parsedPosts, threads_per_batch)
        postsToDB = parsePosts(parsedPosts, originalPostContent)
        print(postsToDB)
        sendPostsToDB(postsToDB)
    else:
        print("No New Reward Applicants Yet, trying again in 30 mins")
# # -----------------------------