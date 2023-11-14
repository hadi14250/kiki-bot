import getpass
import os

def getUsernameInput():
    proxyUsername = input("Enter your proxy username: ")
    # proxyPassword = getpass.getpass("Enter your proxy password: ")
    return proxyUsername

def	getPasswordInput():
    proxyPassword = getpass.getpass("Enter your proxy password: ")
    return proxyPassword


def	getProxyUsername():
	proxyUsername = os.environ.get("proxyUsername")
	if not (proxyUsername):
		proxyUsername = getUsernameInput()
	return (proxyUsername)
	
def	getProxyPassword():
	proxyPassword = os.environ.get("proxyPassword")
	if not (proxyPassword):
		proxyPassword = getPasswordInput()
	return (proxyPassword)
