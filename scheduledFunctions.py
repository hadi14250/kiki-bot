from parseSocialMediaGetRequest import parseSocialMediaGetRequest
from getSocialMediaQueue import getSocialMediaQueue, runSocialMediaThreads, parseFollowers, sendSocialMediaToDB
from getPostQueue import  getPostQueue, runPostThreads, parsePosts, sendPostsToDB
from parsePostsGetRequest import parsePostsGetRequest
from time import sleep
from getCredentials import getAdminJwtTokenEnv
from dotenv import load_dotenv
import requests
import json
import os
from logger import startLogger

logger = startLogger()

# load_dotenv()

def getCampaignetApiDomain():
    domain = os.environ.get("API_DOMAIN")
    if domain != None:
        campaigneUrl = domain + "/api/campaign/paginate/true"
    else:
        raise Exception("API Domain is None")
    return (campaigneUrl)

campaigneUrl = getCampaignetApiDomain()

def returnCampaignContentFromPaginate():
    campaigneBody = {
        "order": "ASC",
        "page": 1,
        "take": 10
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(campaigneUrl, data=json.dumps(campaigneBody), headers=headers)
    
    if response.status_code in [200, 201]:
        data = response.json().get("data", [])
        content = ""  # Initialize content variable outside the loop
        
        for item in data:
            content = item.get("content", "")
        
        return content
    else:
        logger.error(f"Failed to retrieve campaign content with status code: {response.status_code}", exc_info=True)
        logger.error(response.text, exc_info=True)
        return None


threads_per_batch = 250

# # ---------> Social Media get request and then parse to a json object (SocialMediaAccountsToDB) that will be sent to queue <----------
def runSocialMediaScheduler():
    socialMediaResponseJson = getSocialMediaQueue()
    if (socialMediaResponseJson != None):
        logger.info("someone signed up")
        parsedSocialMediaAccounts = parseSocialMediaGetRequest(socialMediaResponseJson)
        runSocialMediaThreads(parsedSocialMediaAccounts, threads_per_batch)
        SocialMediaAccountsToDB = parseFollowers(parsedSocialMediaAccounts)
        sendSocialMediaToDB(SocialMediaAccountsToDB)
# -----------------------------


# # ---------> Posts get request and then parse to a json object (postsToDB) that will be sent to queue <----------
def runPostScheduler():
    originalPostContent = returnCampaignContentFromPaginate()
    if (originalPostContent is None) or (originalPostContent.strip() == ""):
        logger.info("No Active campaigne yet, checking again in 30 minutes")
        return ("NONE")
    postResponseJson = getPostQueue()
    if (postResponseJson != None):
        logger.info("Someone Applied for a reward")
        parsedPosts = parsePostsGetRequest(postResponseJson)
        runPostThreads(parsedPosts, threads_per_batch)
        postsToDB = parsePosts(parsedPosts, originalPostContent)
        sendPostsToDB(postsToDB)
# # -----------------------------
