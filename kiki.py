import urllib.request
import socket
import time
import sys

timeout = 10

shortRestTime  = 1
longRestTime = 10
tenUserInterval = 30
hundredUserInterval = 60
thousandUserInterval = 600


userNum = 102

i = 1

#  -----------> user <---------- 
while i <= userNum:
    try:
        fp = urllib.request.urlopen("https://www.instagram.com/p/CuhDVBQt5P4/?img_index=1", timeout=timeout)
        mybytes = fp.read()
        mystr1 = mybytes.decode("utf8")
        fp.close()
        with open("instagram.html", "w") as file:
            file.write(mystr1)

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mInstagram For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
        else:
            sys.stderr.write("\033[91mInstagram For User {}, URL Error: {}\n\033[0m".format(i, e))
    except Exception as e:
        sys.stderr.write("\033[91mInstagram For User {}, Something went wrong: {}\n\033[0m".format(i, e))

    time.sleep(shortRestTime)

    try:
        fp = urllib.request.urlopen("https://www.tiktok.com/@salzabilll_/video/7297133409426590982", timeout=timeout)
        mybytes = fp.read()
        mystr1 = mybytes.decode("utf8")
        fp.close()
        with open("tiktok.html", "w") as file:
            file.write(mystr1)

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mTiktok For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
        else:
            sys.stderr.write("\033[91mTiktok For User {}, URL Error: {}\n\033[0m".format(i, e))
    except Exception as e:
        sys.stderr.write("\033[91mTiktok For User {}, Something went wrong: {}\n\033[0m".format(i, e))

    time.sleep(shortRestTime)

    try:
        fp = urllib.request.urlopen("https://www.facebook.com/zuck/posts/pfbid02H6zic124gqoP8YqarK3g6CcWA4erRbh51VkM3mV83mQdbxSwovqNtY85vqBwnBael", timeout=timeout)
        mybytes = fp.read()
        mystr1 = mybytes.decode("utf8")
        fp.close()
        with open("facebook.html", "w") as file:
            file.write(mystr1)

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mFacebook For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
        else:
            sys.stderr.write("\033[91mFacebook For User {}, URL Error: {}\n\033[0m".format(i, e))
    except Exception as e:
        sys.stderr.write("\033[91mFacebook For User {}, Something went wrong: {}\n\033[0m".format(i, e))

    time.sleep(shortRestTime)

    try:
        fp = urllib.request.urlopen("https://www.instagram.com/p/CuhDVBQt5P4/?img_index=1", timeout=timeout)
        mybytes = fp.read()
        mystr1 = mybytes.decode("utf8")
        fp.close()
        with open("instagram.html", "w") as file:
            file.write(mystr1)

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mInstagram For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
        else:
            sys.stderr.write("\033[91mInstagram For User {}, URL Error: {}\n\033[0m".format(i, e))
    except Exception as e:
        sys.stderr.write("\033[91mInstagram For User {}, Something went wrong: {}\n\033[0m".format(i, e))

    time.sleep(shortRestTime)

    try:
        fp = urllib.request.urlopen("https://www.tiktok.com/@salzabilll_/video/7297133409426590982", timeout=timeout)
        mybytes = fp.read()
        mystr1 = mybytes.decode("utf8")
        fp.close()
        with open("tiktok.html", "w") as file:
            file.write(mystr1)

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mTiktok For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
        else:
            sys.stderr.write("\033[91mTiktok For User {}, URL Error: {}\n\033[0m".format(i, e))
    except Exception as e:
        sys.stderr.write("\033[91mTiktok For User {}, Something went wrong: {}\n\033[0m".format(i, e))

    time.sleep(shortRestTime)

    try:
        fp = urllib.request.urlopen("https://www.facebook.com/zuck/posts/pfbid02H6zic124gqoP8YqarK3g6CcWA4erRbh51VkM3mV83mQdbxSwovqNtY85vqBwnBael", timeout=timeout)
        mybytes = fp.read()
        mystr1 = mybytes.decode("utf8")
        fp.close()
        with open("facebook.html", "w") as file:
            file.write(mystr1)

    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91mFacebook For User {}, The request timed out after {} seconds.\n\033[0m".format(i, timeout))
        else:
            sys.stderr.write("\033[91mFacebook For User {}, URL Error: {}\n\033[0m".format(i, e))
    except Exception as e:
        sys.stderr.write("\033[91mFacebook For User {}, Something went wrong: {}\n\033[0m".format(i, e))
    #  -----------> user <---------- 

    print(f"\033[92mUser Number {i} finished.\033[0m")

    if (i % 1000 == 0 and i != userNum):
        print("\033[1m{} Users Done, Resting for {} seconds\033[0m".format(i, thousandUserInterval))
        time.sleep(thousandUserInterval)
    if (i % 100 == 0 and i != userNum):
        print("\033[94m{} Users Done, Resting for {} seconds\033[0m".format(i, hundredUserInterval))
        time.sleep(hundredUserInterval)
    elif (i % 10 == 0 and i != userNum):
        print("\033[93m{} Users Done, Resting for {} seconds\033[0m".format(i, tenUserInterval))
        time.sleep(tenUserInterval)
    elif (i != userNum):
        time.sleep(longRestTime)

    i += 1


