import requests
from getCredentials import getAdminEmail, getAdminPassword
from logger import startLogger
import os
logger = startLogger()

def getAdminApiDomain():
    domain = os.environ.get("API_DOMAIN")
    if domain != None:
        adminUrl = domain + "/api/auth/login"
    else:
        raise Exception("API Domain is None")
    return (adminUrl)

def getBotApiDomain():
    domain = os.environ.get("API_DOMAIN")
    if domain != None:
        botUrl = domain + "/api/bot/token"
    else:
        raise Exception("API Domain is None")
    return (botUrl)

adminUrl = getAdminApiDomain()

botUrl = getBotApiDomain()

timeout = 60

def getAdminToken():
    try:
        payload = {
        "login": getAdminEmail(),
        "password": getAdminPassword()
        }
        response = requests.post(adminUrl, json=payload, timeout=timeout)
        # Check the response status
        if (response.status_code == 200):
            response_json = response.json()
            jwt_token = response_json.get("token")
            return (jwt_token)
        else:
            logger.error(f"admin jwt token Request failed with status code: {response.status_code}", exc_info=True)
            logger.error(response.text, exc_info=True)
    except:
        logger.error(f"admin jwt token Request failed with status code: {response.status_code}", exc_info=True)
        logger.error(response.text, exc_info=True)

def getBotToken(admin_jwt_token):
    try:
        headers = {
            "Authorization": f"Bearer {admin_jwt_token}"
        }
        response = requests.get(botUrl, headers=headers)
        if (response.status_code == 200):
            response_json = response.json()
            jwt_token = response_json.get("token")
            return (jwt_token)
        else:
            logger.error(f"bot jwt token Request failed with status code: {response.status_code}", exc_info=True)
            logger.error(response.text, exc_info=True)
    except:
            logger.error(f"bot jwt token Request failed with status code: {response.status_code}", exc_info=True)
            logger.error(response.text, exc_info=True)


def setAdminJwtToken(token):
    with open(".env", "r") as f:
        lines = f.readlines()
    found = False
    for i, line in enumerate(lines):
        if line.startswith("ADMIN_JWT_TOKEN="):
            lines[i] = f"ADMIN_JWT_TOKEN={token}\n"
            found = True

    if not found:
        lines.append(f"ADMIN_JWT_TOKEN={token}\n")

    with open(".env", "w") as f:
        f.writelines(lines)

def setBotJwtToken(token):
    with open(".env", "r") as f:
        lines = f.readlines()

    found = False
    for i, line in enumerate(lines):
        if line.startswith("BOT_JWT_TOKEN="):
            lines[i] = f"BOT_JWT_TOKEN={token}\n"
            found = True

    if not found:
        lines.append(f"BOT_JWT_TOKEN={token}\n")

    with open(".env", "w") as f:
        f.writelines(lines)
