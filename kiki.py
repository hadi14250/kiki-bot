import urllib.request
import socket
import time
import sys
import os
import requests
from utils import requestsFallback

timeout = 20

shortRestTime  = 1
longRestTime = 5
fiveUserInterval = 10
hundredUserInterval = 60
thousandUserInterval = 600


userNum = 102

i = 1

headers = {
    'User-Agent': 'My User Agent 1.0',
    'From': 'youremail@domain.example'  # This is another valid field
}

#  -----------> user <---------- 
while i <= userNum:
    try:
        url = "https://www.instagram.com/p/CuhDVBQt5P4/?img_index=1"
        fp = urllib.request.urlopen(url, timeout=timeout)
        mybytes = fp.read()
        htmlText = mybytes.decode("utf8")
        fp.close()

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mInstagram For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
            htmlText = requestsFallback(i, url, timeout, headers)
        else:
            sys.stderr.write("\033[91mInstagram For User {}, URL Error: {}\n\033[0m".format(i, e))
            htmlText = requestsFallback(i, url, timeout, headers)
    except Exception as e:
        sys.stderr.write("\033[91mInstagram For User {}, Something went wrong: {}\n\033[0m".format(i, e))
        htmlText = requestsFallback(i, url, timeout, headers)

    with open("instagram.html", "w") as file:
        file.write(htmlText)
    
    time.sleep(shortRestTime)

    try:
        url = "https://www.tiktok.com/@salzabilll_/video/7297133409426590982"
        fp = urllib.request.urlopen(url, timeout=timeout)
        mybytes = fp.read()
        htmlText = mybytes.decode("utf8")
        fp.close()

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mTiktok For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
            htmlText = requestsFallback(i, url, timeout, headers)
        else:
            sys.stderr.write("\033[91mTiktok For User {}, URL Error: {}\n\033[0m".format(i, e))
            htmlText = requestsFallback(i, url, timeout, headers)
    except Exception as e:
        sys.stderr.write("\033[91mTiktok For User {}, Something went wrong: {}\n\033[0m".format(i, e))
        htmlText = requestsFallback(i, url, timeout, headers)

    with open("tiktok.html", "w") as file:
            file.write(htmlText)

    time.sleep(shortRestTime)

    try:
        url = "https://www.facebook.com/zuck/posts/pfbid02H6zic124gqoP8YqarK3g6CcWA4erRbh51VkM3mV83mQdbxSwovqNtY85vqBwnBael"
        fp = urllib.request.urlopen(url, timeout=timeout)
        mybytes = fp.read()
        htmlText = mybytes.decode("utf8")
        fp.close()

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mFacebook For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
            htmlText = requestsFallback(i, url, timeout, headers)
        else:
            sys.stderr.write("\033[91mFacebook For User {}, URL Error: {}\n\033[0m".format(i, e))
            htmlText = requestsFallback(i, url, timeout, headers)
    except Exception as e:
        sys.stderr.write("\033[91mFacebook For User {}, Something went wrong: {}\n\033[0m".format(i, e))
        htmlText = requestsFallback(i, url, timeout, headers)

    with open("facebook.html", "w") as file:
        file.write(htmlText)

    time.sleep(shortRestTime)

    try:
        url = "https://www.instagram.com/p/CuhDVBQt5P4/?img_index=1"
        fp = urllib.request.urlopen(url, timeout=timeout)
        mybytes = fp.read()
        htmlText = mybytes.decode("utf8")
        fp.close()

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mInstagram For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
            htmlText = requestsFallback(i, url, timeout, headers)
        else:
            sys.stderr.write("\033[91mInstagram For User {}, URL Error: {}\n\033[0m".format(i, e))
            htmlText = requestsFallback(i, url, timeout, headers)
    except Exception as e:
        sys.stderr.write("\033[91mInstagram For User {}, Something went wrong: {}\n\033[0m".format(i, e))
        htmlText = requestsFallback(i, url, timeout, headers)

    with open("instagram.html", "w") as file:
        file.write(htmlText)
   
    time.sleep(shortRestTime)

    try:
        url = "https://www.tiktok.com/@salzabilll_/video/7297133409426590982"
        fp = urllib.request.urlopen(url, timeout=timeout)
        mybytes = fp.read()
        htmlText = mybytes.decode("utf8")
        fp.close()

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mTiktok For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
            htmlText = requestsFallback(i, url, timeout, headers)
        else:
            sys.stderr.write("\033[91mTiktok For User {}, URL Error: {}\n\033[0m".format(i, e))
            htmlText = requestsFallback(i, url, timeout, headers)
    except Exception as e:
        sys.stderr.write("\033[91mTiktok For User {}, Something went wrong: {}\n\033[0m".format(i, e))
        htmlText = requestsFallback(i, url, timeout, headers)

    with open("tiktok.html", "w") as file:
        file.write(htmlText)

    time.sleep(shortRestTime)

    try:
        url = "https://www.facebook.com/zuck/posts/pfbid02H6zic124gqoP8YqarK3g6CcWA4erRbh51VkM3mV83mQdbxSwovqNtY85vqBwnBael"
        fp = urllib.request.urlopen(url, timeout=timeout)
        mybytes = fp.read()
        htmlText = mybytes.decode("utf8")
        fp.close()

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mFacebook For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
            htmlText = requestsFallback(i, url, timeout, headers)
        else:
            sys.stderr.write("\033[91mFacebook For User {}, URL Error: {}\n\033[0m".format(i, e))
            htmlText = requestsFallback(i, url, timeout, headers)
    except Exception as e:
        sys.stderr.write("\033[91mFacebook For User {}, Something went wrong: {}\n\033[0m".format(i, e))
        htmlText = requestsFallback(i, url, timeout, headers)
    
    with open("facebook.html", "w") as file:
        file.write(htmlText)
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