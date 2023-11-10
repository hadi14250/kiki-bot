from bs4 import BeautifulSoup
import requests
import urllib.request

url = "https://instagram.com/pubity/"

def getting_parsa_data(i):
    data = {}
    i = i.split("_")[0]
    i = i.split(" ")
    data["Followers"] = i[0]
    data["followers"] = i[1]
    data["Following"] = i[2]
    data["following"] = i[3]
    data["Posts"] = i[4]
    data["posts"] = i[5]
    return data

def getting_scrape_data(htmlText):
    i = BeautifulSoup(htmlText, "html.parser")
    meta = i.find("meta", property="og:description")
    return getting_parsa_data(meta.attrs['content'])
