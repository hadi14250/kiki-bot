import urllib.request
import socket
import time
import sys
import os
import requests
from requests.exceptions import RequestException

def requestsFallback(i, url, timeout, headers):
    try:
        print("\033[38;5;208mRetrying for user {} with requests.get() method instead...\033[0m".format(i))
        time.sleep(10)
        r = requests.get(url, headers=headers, timeout=timeout)
        r.raise_for_status()
        print(f"\033[35mSuccess for User {i} using requests.get() method! ✅ \033[0m")
        with open("backUp.html", "w") as file:
            file.write(r.text)
        return r.text
    except requests.ConnectionError as e:
        sys.stderr.write("\033[91mrequests.get() method for User {}, did not work, error os: {}\n\033[0m".format(i, e))
        return None
    except RequestException as e:
        print(f"An error occurred: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    except requests.exceptions.SSLError as e:
        print(f"SSL/TLS handshake error: {e}")
        return None
    except requests.exceptions.Timeout as e:
        print(f"Request timed out: {e}")
        return None

def reqInstaUrl(i, url, timeout, headers, socialMedia):
    try:
        fp = urllib.request.urlopen(url, timeout=timeout)
        mybytes = fp.read()
        fp.close()
        htmlText = mybytes.decode("utf8")
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            sys.stderr.write("\033[91m{} For User {}, The request timed out after {} seconds.\n\033[0m".format(socialMedia, i, timeout))
            htmlText = requestsFallback(i, url, timeout, headers)
        else:
            sys.stderr.write("\033[91m{} For User {}, URL Error: {}\n\033[0m".format(socialMedia, i, e))
            htmlText = requestsFallback(i, url, timeout, headers)
    except Exception as e:
        sys.stderr.write("\033[91m{} For User {}, Something went wrong: {}\n\033[0m".format(socialMedia, i, e))
        htmlText = requestsFallback(i, url, timeout, headers)
    return (htmlText)