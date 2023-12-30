import os
from dotenv import load_dotenv

# load_dotenv()

def	getProxyUsername():
	proxyUsername = os.environ.get("PROXY_USERNAME")
	if not (proxyUsername):
		return (None)
	return (proxyUsername)
	
def	getProxyPassword():
	proxyPassword = os.environ.get("PROXY_PW")
	if not (proxyPassword):
		return (None)
	return (proxyPassword)


def	getAdminEmail():
	adminEmail = os.environ.get("ADMIN_EMAIL")
	if not (adminEmail):
		return (None)
	return (adminEmail)

def	getAdminPassword():
	admin_PW = os.environ.get("ADMIN_PW")
	if not (admin_PW):
		return (None)
	return (admin_PW)


def	getBotJwtTokenEnv():
	botJwtToken = os.environ.get("BOT_JWT_TOKEN")
	if not (botJwtToken):
		return (None)
	return (botJwtToken)
	

def	getAdminJwtTokenEnv():
	adminJwtToken = os.environ.get("ADMIN_JWT_TOKEN")
	if not (adminJwtToken):
		return (None)
	return (adminJwtToken)



	
