from dotenv import load_dotenv
from getTokensAndSetEnv import getAdminToken, getBotToken, setAdminJwtToken, setBotJwtToken
from getCredentials import getAdminJwtTokenEnv, getBotJwtTokenEnv

# getting tokens and loading them into the .env and the environment

# Loads .env into envirnment
load_dotenv()
adminToken = getAdminToken()
botToken = getBotToken(adminToken)
setAdminJwtToken(adminToken)
setBotJwtToken(botToken)
if not (adminToken) or not (botToken):
    print("can't aquire admin tokens")
    exit()