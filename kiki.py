import urllib.request
import socket
import time
import sys
import os
import requests
from utils import requestsFallback, reqInstaUrl, restFetch

import pandas as pd
from openpyxl import load_workbook
from user import User, user_objects

timeout = 10

shortRestTime  = 1
longRestTime = 5
fiveUserInterval = 10
hundredUserInterval = 60
thousandUserInterval = 600

# shortRestTime  = 0.1
# longRestTime = 0.1
# fiveUserInterval = 0.1
# hundredUserInterval = 60
# thousandUserInterval = 600

# userNum = len(user_objects)
userNum = 6
print("Total User in excel Sheet: {}".format(userNum))

i = 1

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.example'  # This is another valid field
}

#  -----------> user <---------- 
for user in user_objects[:userNum]:

    #   ---> instagram Profile<---

    url = user.insta.profileUrl
    if not(pd.isna(url)):
        user.insta.status = True
    
    if (user.insta.status == True):
        htmlText = reqInstaUrl(user.UserNum, url, timeout, headers, "Instagram Profile")
        if (htmlText != None):
            with open("instagramProfile.html", "w") as file:
                file.write(htmlText)
        time.sleep(shortRestTime)
    else:
        print(f"User Number {user.UserNum}, {user.fullName}, does not have an instagram field")

    #   ---> tiktok Profile<---
    
    url = user.tiktok.profileUrl
    if not(pd.isna(url)):
        user.tiktok.status = True
    if (user.tiktok.status == True):
        htmlText = reqInstaUrl(user.UserNum, url, timeout, headers, "Tiktok Profile")
        if (htmlText != None):
            with open("tiktokProfile.html", "w") as file:
                    file.write(htmlText)
        time.sleep(shortRestTime)
    else:
        print(f"User Number {user.UserNum}, {user.fullName}, does not have an tiktok field")

    #   ---> instagram Post<---
    url = user.insta.postUrl
    if (user.insta.status == True):
        htmlText = reqInstaUrl(user.UserNum, url, timeout, headers, "Instagram Post")
        if (htmlText != None):
            with open("instagramPost.html", "w") as file:
                file.write(htmlText)
        time.sleep(shortRestTime)
    else:
        print(f"Skipping Instagram post for {user.fullName} as no profile url specified")

    #   ---> tiktok Post<---
    url = user.tiktok.postUrl
    if (user.tiktok.status == True):
        htmlText = reqInstaUrl(i, url, timeout, headers, "Tiktok Post")
        if (htmlText != None):
            with open("tiktokPost.html", "w") as file:
                    file.write(htmlText)
    else:
        print(f"Skipping tiktok post for {user.fullName} as no profile url specified")

    print(f"\033[92mUser Number {user.UserNum}, {user.fullName} finished.\033[0m")

    restFetch(i, longRestTime, fiveUserInterval,
              hundredUserInterval, thousandUserInterval)

    i += 1

'''
os.remove("instagram.html")
os.remove("facebook.html")
os.remove("tiktok.html")

'''