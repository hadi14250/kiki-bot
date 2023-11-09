import os
import sys
import pandas as pd
from openpyxl import load_workbook


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
    def __init__(self, url, followers, post_url, post_like, post_tags, payment):
        self.profileUrl = url
        self.followers = followers
        self.postUrl = post_url
        self.postLike = post_like
        self.postTags = post_tags
        self.payment = payment
        self.status = None


class User:
    def __init__(self, user_num, full_name, insta, tiktok, facebook, total_prize, walletAdd):
        self.UserNum = user_num
        self.fullName = full_name
        self.insta = insta
        self.tiktok = tiktok
        self.facebook = facebook
        self.totalPrize = total_prize
        self.walletAdd = walletAdd


# Load the Excel file
file_name = "user_data.xlsx"
file_path = get_absolute_file_path(file_name)
sheet_name = "users"
df = pd.read_excel(file_path, sheet_name=sheet_name, engine="openpyxl")

# Create User objects from the Excel data
user_objects = []
for index, row in df.iterrows():
    insta_profile = SocialMediaProfile(
        url=row["Insta_url"],
        followers=row["Insta_followers"],
        post_url=row["Insta_post_url"],
        post_like=row["Insta_post_like"],
        post_tags=row["Insta_post_tags"],
        payment=row["Insta_payment"]
    )
    tiktok_profile = SocialMediaProfile(
        url=row["TikTok_url"],
        followers=row["TikTok_followers"],
        post_url=row["TikTok_post_url"],
        post_like=row["TikTok_post_like"],
        post_tags=row["TikTok_post_tags"],
        payment=row["TikTok_payment"]
    )
    facebook_profile = SocialMediaProfile(
        url=row["Facebook_url"],
        followers=row["Facebook_followers"],
        post_url=row["Facebook_post_url"],
        post_like=row["Facebook_post_like"],
        post_tags=row["Facebook_post_tags"],
        payment=row["Facebook_payment"]
    )
    user_object = User(
        user_num=row["UserNum"],
        full_name=row["fullName"],
        insta=insta_profile,
        tiktok=tiktok_profile,
        facebook=facebook_profile,
        total_prize=row["totalPrize"],
        walletAdd=row["Wallet Address"]
    )
    user_objects.append(user_object)


# userNum = 13
# i = 1
# # Now user_objects is a list containing User objects for all users
# for user in user_objects[:userNum]:
#     print("UserNum:", user.UserNum)
#     print("Full Name:", user.fullName)
#     print("Instagram Profile URL:", user.insta.profileUrl)
#     print("Instagram Followers:", user.insta.followers)
#     print("Instgram Tags:", user.insta.postTags)
#     print("Tiktok Profile Url:", user.tiktok.profileUrl)
#     print("Tiktok Followers:", user.tiktok.followers)
#     print("Total Prize:", user.totalPrize)
#     print("{}'s Wallet Address:".format(user.fullName), user.walletAdd)
#     print("-------------")
#     i += 1

print("\033[92mData from excel Sheet reading done\033[0m")