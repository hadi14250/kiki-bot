import requests

url = "http://localhost:3000/api/auth/login"
payload = {
    "login": "scom@scomcoin.io",
    "password": "E2DVw&F@"
}

# Send POST request
response = requests.post(url, json=payload)

# Check the response status
if (response.status_code == 200):
    response_json = response.json()
    jwt_token = response_json.get("token")
    print(f"Admin Token: {jwt_token}")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)



url = "http://localhost:3000/api/bot/token"
headers = {
    "Authorization": f"Bearer {jwt_token}"
}


response = requests.get(url, headers=headers)

bot_jwt_token = response_json.get("token")
print("Bot token: ", bot_jwt_token)



url = "http://localhost:3000/api/bot/social"
headers = {
    "accept": "*/*",
    "Authorization": f"Bearer {bot_jwt_token}"
}

response = requests.get(url, headers=headers)

if (response.status_code == 200):
    response_json = response.json()
    jwt_token = response_json.get("token")
    print(f"Admin Token: {jwt_token}")
else:
    print(f"Request failed with status code: {response.status_code}")
    print(response.text)