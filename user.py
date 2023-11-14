import os
import sys
import pandas as pd
from openpyxl import load_workbook
from constructUrls import constructInstagramUrl, constructTiktokUrl, constructTwitterUrl
from extractInstaProfileData import getInstaFollowers
from extractInstaPostData import extractInstaPostData
from formatHtml import formatHtml

def get_program_path():
    # Get the path to the currently running Python script
    script_path = os.path.abspath(sys.argv[0])
    # Extract the directory path
    program_path = os.path.dirname(script_path)
    return program_path

def get_absolute_file_path(file_name):
    program_path = get_program_path()
    file_path = os.path.join(program_path, file_name)
    return os.path.abspath(file_path)


class SocialMediaProfile:
	def __init__(self, csvUserName):
		self.csvUserName 		= csvUserName
		self.profileUrl			= None
		self.response			= None
		self.html				= None
		self.followers 			= 0
		self.registerDate		= None

	def setScrapedData(self, type):
		if (type == "instagram"):
			self.followers = getInstaFollowers(self.html)
	def	formatHtmlResponse(self, response):
		self.response = response
		self.html = formatHtml(response.text)


class SocialMediaPost:
	def __init__(self, post_url):
		self.postUrl 			= post_url
		self.response			= None
		self.html				= None
		self.excractedUserName	= None
		self.postLike			= 0
		self.postText			= None
		self.postTags			= None
		self.postDate			= None
		self.payment			= 0

	def setScrapedData(self, type):
		if (type == "instagram"):
			self.excractedUserName	= extractInstaPostData(self.html, "userName")
			self.postLike			= extractInstaPostData(self.html, "likeCount")
			self.postText			= extractInstaPostData(self.html, "content")
			self.postDate			= extractInstaPostData(self.html, "postDate")
			# self.postTags			= not yet done
	def	formatHtmlResponse(self, response):
		self.response = response
		self.html = formatHtml(response.text)




class User:
	def __init__(self, user_num, full_name, instaProfile, instaPost,
			  		tiktokProfile, tiktokPost, twitterProfile,
					tweet, walletAdd):
		self.UserNum		= user_num
		self.fullName		= full_name
		self.instaProfile	= instaProfile
		self.instaPost		= instaPost
		self.tiktokProfile	= tiktokProfile
		self.tiktokPost		= tiktokPost
		self.twitterProfile	= twitterProfile
		self.tweet			= tweet
		self.walletAdd		= walletAdd
		self.proxyJobID		= None

# Load the Excel file
file_name = "user_data.xlsx"
file_path = get_absolute_file_path(file_name)
sheet_name = "users"
df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")

# Create User objects from the Excel data
user_objects = []
for index, row in df.iterrows():
    instaProfile = SocialMediaProfile(
        csvUserName = row["Insta_user_name"],
    )
    instaPost = SocialMediaPost(
        post_url = row["Insta_post_url"],
    )

    tiktokProfile = SocialMediaProfile(
        csvUserName = row["tiktok_username"],
    )
    tiktokPost = SocialMediaPost(
        post_url = row["TikTok_post_url"],
    )

    twitterProfile = SocialMediaProfile(
        csvUserName = row["Twitter_handle"],
    )
    tweet = SocialMediaPost(
        post_url = row["Twitter_post_url"],
    )

    user_object = User(
        user_num		= row["UserNum"],
        full_name		= row["fullName"],
        instaProfile	= instaProfile,
		instaPost		= instaPost,
        tiktokProfile	= tiktokProfile,
		tiktokPost		= tiktokPost,
        twitterProfile	= twitterProfile,
		tweet			= tweet,
        walletAdd		= row["Wallet Address"]
    )
    user_objects.append(user_object)


def	printUserInfo():
	for user in user_objects:
		print("Instagram Profile Username: {}, url: {}".format(
			user.instaProfile.csvUserName, user.instaProfile.profileUrl
		))

		print("Instagram post url: {}".format(user.instaPost.postUrl))

		print("Tiktok Profile Username: {}, url: {}".format(
			user.tiktokProfile.csvUserName, user.tiktokProfile.profileUrl
		))

		print("Tiktok post url: {}".format(user.tiktokPost.postUrl))

		print("Twitter Profile Username: {}, url: {}".format(
			user.twitterProfile.csvUserName, user.twitterProfile.profileUrl
		))

		print("Tweet url: {}".format(user.tweet.postUrl))

# Now user_objects is a list containing User objects for all users
for user in user_objects:
	user.instaProfile.profileUrl = constructInstagramUrl(user.instaProfile.csvUserName)
	user.tiktokProfile.profileUrl = constructTiktokUrl(user.tiktokProfile.csvUserName)
	user.twitterProfile.profileUrl = constructTwitterUrl(user.twitterProfile.csvUserName)

# printUserInfo()

print("\033[92mData from excel Sheet reading done\033[0m")