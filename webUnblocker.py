import requests

# Define proxy dict. Don't forget to put your real user and pass here as well.
proxies = {
  'http': 'http://hadi14250:05590560352Hk200018@unblock.oxylabs.io:60000',
  'https': 'http://hadi14250:05590560352Hk200018@unblock.oxylabs.io:60000',
}

twitterHandle = "ordinalHO"
twitterSession = "?t=gfu&s=08654"
url = "https://twitter.com/{}{}".format(twitterHandle, twitterSession)


response = requests.request(
    'GET',
    "https://x.com/{}{}".format(twitterHandle, twitterSession),
    verify=False,  # Ignore the certificate
    proxies=proxies,
)

# Save returned HTML to result.html file
with open('webUnblocker.html', 'w') as f:
    f.write(response.text)