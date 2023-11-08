import requests
import sys
import time

def requestsFallback(i, url, timeout, headers):
    try:
        print("\033[38;5;208mRetrying for user {} with requests.get() method instead...\033[0m".format(i))
        time.sleep(10)
        r = requests.get(url, headers=headers, timeout=timeout)
        print(f"\033[35mSuccess for User {i} using requests.get() method! ✅ \033[0m")
    except requests.ConnectionError as e:
        sys.stderr.write("\033[91mrequests.get() method for User {}, did not work, error os: {}\n\033[0m".format(i, e))
    
    with open("backUp.html", "w") as file:
        file.write(r.text)
    return r.text
