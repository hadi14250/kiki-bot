import pandas as pd

global instaUrlArg
instaUrlArg = "?igshid=OGQ5ZDc2ODk2ZA=="

global tiktokUrlArg
tiktokUrlArg = "?_t=8hHhujoZ2Kv&_r=1"

global twitterUrlArg
twitterUrlArg = "?t=Qp2Nf21GbEky-cSABxUEYg&s=08"

def constructInstagramUrl(username):
    if (pd.isna(username)):
        return None
    url = "https://instagram.com/{}{}".format(username, instaUrlArg)
    return url

def constructTiktokUrl(username):
    if (pd.isna(username)):
        return None
    if '@' in username:
        url = "https://www.tiktok.com/{}{}".format(username, tiktokUrlArg)
    else:
        url = "https://www.tiktok.com/@{}{}".format(username, tiktokUrlArg)
    return url

def constructTwitterUrl(username):
    if (pd.isna(username)):
        return None
    url = "https://x.com/{}{}".format(username, twitterUrlArg)
    return url
