import urllib.request
import socket
import time
import sys
import os
import requests
from utils import requestsFallback
from utils import reqInstaUrl
import pandas as pd
from openpyxl import load_workbook

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

userNum = 101

i = 1

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.example'  # This is another valid field
}

#  -----------> user <---------- 
while i <= userNum:

    #   ---> instagram Profile<---
    url = "https://www.instagram.com/takeovr23/?igshid=MXJucG91aXgyMnhpZg%3D%3D"
    
    htmlText = reqInstaUrl(i, url, timeout, headers, "Instagram Profile")

    if (htmlText != None):
        with open("instagramProfile.html", "w") as file:
            file.write(htmlText)
    
    time.sleep(shortRestTime)

    #   ---> tiktok Profile<---
    url = "https://www.tiktok.com/@thezachchoi"

    htmlText = reqInstaUrl(i, url, timeout, headers, "Tiktok Profile")
    
    if (htmlText != None):
        with open("tiktokProfile.html", "w") as file:
                file.write(htmlText)

    time.sleep(shortRestTime)

    #   ---> facebook Profile<---
    # url = "https://www.facebook.com/photo?fbid=868551677967530&set=a.285784912910879"

    # htmlText = reqInstaUrl(i, url, timeout, headers, "Facebook Profile")

    # if (htmlText != None):
    #     with open("facebookProfile.html", "w") as file:
    #        file.write(htmlText)

    # time.sleep(shortRestTime)

    #   ---> instagram Post<---
    url = "https://www.instagram.com/p/CzTWqUWLLvJ/"

    htmlText = reqInstaUrl(i, url, timeout, headers, "Instagram Post")

    if (htmlText != None):
        with open("instagramPost.html", "w") as file:
            file.write(htmlText)
    
    time.sleep(shortRestTime)

    #   ---> tiktok Post<---
    url = "https://www.tiktok.com/@thezachchoi/video/7298038955348397354"

    htmlText = reqInstaUrl(i, url, timeout, headers, "Tiktok Post")
    
    if (htmlText != None):
        with open("tiktokPost.html", "w") as file:
                file.write(htmlText)

    # time.sleep(shortRestTime)

    # #   ---> facebook Post<---
    # url = "https://www.facebook.com/zuck/posts/pfbid0D5Q18BpW1php3hPmVeJznSQHExp7WJEQLEECj9g5eQuoddmP8MvLFK5qGE76HoL1l"

    # htmlText = reqInstaUrl(i, url, timeout, headers, "Facebook Post")

    # if (htmlText != None):
    #     with open("facebookPost.html", "w") as file:
    #         file.write(htmlText)
    #  -----------> user <---------- 

    print(f"\033[92mUser Number {i} finished.\033[0m")

    if (i % 1000 == 0 and i != userNum):
        print("\033[1m{} Users Done, Resting for {} seconds\033[0m".format(i, thousandUserInterval))
        time.sleep(thousandUserInterval)
    elif (i % 100 == 0 and i != userNum):
        print("\033[94m{} Users Done, Resting for {} seconds\033[0m".format(i, hundredUserInterval))
        time.sleep(hundredUserInterval)
    elif (i % 5 == 0 and i != userNum):
        print("\033[93m{} Users Done, Resting for {} seconds\033[0m".format(i, fiveUserInterval))
        time.sleep(fiveUserInterval)
    elif (i != userNum):
        time.sleep(longRestTime)

    i += 1

'''
os.remove("instagram.html")
os.remove("facebook.html")
os.remove("tiktok.html")

'''