import os
import sys
import pandas as pd
from openpyxl import load_workbook
from constructUrls import constructInstagramUrl, constructTiktokUrl, constructTwitterUrl

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
    def __init__(self, followers, post_url, post_like, post_tags, payment, userName):
        self.userName = userName
        self.profileUrl = None
        self.followers = followers
        self.postUrl = post_url
        self.postLike = post_like
        self.postTags = post_tags
        self.payment = payment
        self.status = None


class User:
    def __init__(self, user_num, full_name, insta, tiktok, twitter, total_prize, walletAdd):
        self.UserNum = user_num
        self.fullName = full_name
        self.insta = insta
        self.tiktok = tiktok
        self.twitter = twitter
        self.totalPrize = total_prize
        self.walletAdd = walletAdd


def printForTesting(user):
    print("UserNum:", user.UserNum)
    print("Full Name:", user.fullName)
    print("Instagram Profile Username:", user.insta.userName)
    print("Instagram Profile URL:", user.insta.profileUrl)
    print("Tiktok Profile Username:", user.tiktok.userName)
    print("Tiktok Profile Url:", user.tiktok.profileUrl)
    print("Tiktok Followers:", user.tiktok.followers)
    print("twitter Profile Username:", user.twitter.userName)
    print("twitter Profile Url:", user.twitter.profileUrl)
    print("twitter Followers:", user.twitter.followers)
    print("-------------")

# Load the Excel file
file_name = "user_data.xlsx"
file_path = get_absolute_file_path(file_name)
sheet_name = "users"
df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")

# Create User objects from the Excel data
user_objects = []
for index, row in df.iterrows():
    insta_profile = SocialMediaProfile(
        userName = row["Insta_user_name"],
        followers = row["Insta_followers"],
        post_url = row["Insta_post_url"],
        post_like = row["Insta_post_like"],
        post_tags = row["Insta_post_tags"],
        payment = row["Insta_payment"],
    )
    tiktok_profile = SocialMediaProfile(
        userName = row["tiktok_username"],
        followers = row["TikTok_followers"],
        post_url = row["TikTok_post_url"],
        post_like = row["TikTok_post_like"],
        post_tags = row["TikTok_post_tags"],
        payment = row["TikTok_payment"],
    )
    twitter_profile = SocialMediaProfile(
        userName = row["Twitter_handle"],
        followers = row["Twitter_followers"],
        post_url = row["Twitter_post_url"],
        post_like = row["Twitter_post_like"],
        post_tags = row["Twitter_post_tags"],
        payment = row["Twitter_payment"],
    )
    user_object = User(
        user_num=row["UserNum"],
        full_name=row["fullName"],
        insta=insta_profile,
        tiktok=tiktok_profile,
        twitter=twitter_profile,
        total_prize=row["totalPrize"],
        walletAdd=row["Wallet Address"]
    )
    user_objects.append(user_object)



# Now user_objects is a list containing User objects for all users
for user in user_objects:
    user.insta.profileUrl = constructInstagramUrl(user.insta.userName)
    user.tiktok.profileUrl = constructTiktokUrl(user.tiktok.userName)
    user.twitter.profileUrl = constructTwitterUrl(user.twitter.userName)
    # printForTesting(user)



print("\033[92mData from excel Sheet reading done\033[0m")