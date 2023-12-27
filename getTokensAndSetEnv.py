import requests
from getCredentials import getAdminEmail, getAdminPassword

adminUrl = "http://localhost:3000/api/auth/login"
botUrl = "http://localhost:3000/api/bot/token"

# Send POST request
def getAdminToken():
    try:
        payload = {
        "login": getAdminEmail(),
        "password": getAdminPassword()
        }
        response = requests.post(adminUrl, json=payload)
        # Check the response status
        if (response.status_code == 200):
            response_json = response.json()
            jwt_token = response_json.get("token")
            return (jwt_token)
        else:
            print(f"admin jwt token Request failed with status code: {response.status_code}")
            print(response.text)
    except:
        print("Failed to get admin jwt token")


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
            print(f"bot jwt token Request failed with status code: {response.status_code}")
            print(response.text)
    except:
        print("Failed to get bot jwt token")


def setAdminJwtToken(token):
    # Read the existing content of the .env file
    with open(".env", "r") as f:
        lines = f.readlines()

    # Update or add the ADMIN_JWT_TOKEN line
    found = False
    for i, line in enumerate(lines):
        if line.startswith("ADMIN_JWT_TOKEN="):
            lines[i] = f"ADMIN_JWT_TOKEN={token}\n"
            found = True

    if not found:
        lines.append(f"ADMIN_JWT_TOKEN={token}\n")

    # Write the updated content back to the .env file
    with open(".env", "w") as f:
        f.writelines(lines)

def setBotJwtToken(token):
    # Read the existing content of the .env file
    with open(".env", "r") as f:
        lines = f.readlines()

    # Update or add the ADMIN_JWT_TOKEN line
    found = False
    for i, line in enumerate(lines):
        if line.startswith("BOT_JWT_TOKEN="):
            lines[i] = f"BOT_JWT_TOKEN={token}\n"
            found = True

    if not found:
        lines.append(f"BOT_JWT_TOKEN={token}\n")

    # Write the updated content back to the .env file
    with open(".env", "w") as f:
        f.writelines(lines)
