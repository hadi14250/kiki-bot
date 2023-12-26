from parseSocialMediaGetRequest import parseSocialMediaGetRequest
from getSocialMediaQueue import getSocialMediaQueue, runSocialMediaThreads, parseFollowers
from getPostQueue import  getPostQueue, runPostThreads, parsePosts
from parsePostsGetRequest import parsePostsGetRequest

originalPostContent = "🌟 Calling all adventurers! The quest to uncover SCOM's elusive dad, the one and only Reese (aka our dev's dad), is officially underway! 🚀 Join the expedition and be a part of the excitement as we unravel the mystery surrounding his whereabouts. 🕵️‍♂️ Your contribution could be the"
threads_per_batch = 250

# ---------> Social Media get request and then parse to a json object (SocialMediaAccountsToDB) that will be sent to queue <----------
socialMediaResponseJson = getSocialMediaQueue()
parsedSocialMediaAccounts = parseSocialMediaGetRequest(socialMediaResponseJson)
runSocialMediaThreads(parsedSocialMediaAccounts, threads_per_batch)
SocialMediaAccountsToDB = parseFollowers(parsedSocialMediaAccounts)
print(SocialMediaAccountsToDB)
# -----------------------------


# ---------> Posts get request and then parse to a json object (postsToDB) that will be sent to queue <----------
postResponseJson = getPostQueue()
parsedPosts = parsePostsGetRequest(postResponseJson)
runPostThreads(parsedPosts, threads_per_batch)
postsToDB = parsePosts(parsedPosts, originalPostContent)
print(postsToDB)
# -----------------------------