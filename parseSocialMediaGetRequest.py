from constructUrls import constructUrl
from findProxyJobID import findProxyJobID
from formatHtml import formatHtml
from bs4 import BeautifulSoup

class User:
	def __init__(self, scomuserNum, id, socialMedia, socialMediaType, url, scomUserName):
		self.scomuserNum		    = scomuserNum
		self.id		            = id
		self.socialMedia	    = socialMedia
		self.socialMediaType    = socialMediaType
		self.scomUserName       = scomUserName
		self.url                = url
		self.followers          = 0
		self.validated          = False
		self.response			= None
		self.html				= None
		self.soupHtml			= None
		self.proxyJobID         = None

	def	formatHtmlResponse(self, response):
		self.proxyJobID = findProxyJobID(response.text, "job_id")
		self.response = response
		self.html = formatHtml(response.text)
		if (self.html):
			self.soupHtml = BeautifulSoup(self.html, "html.parser")


user_objects = []

def parseSocialMediaGetRequest(response_json):
    for item in response_json:
        scomuserNum = item.get("scomuser")
        user_id = item.get("id")
        socialMedia = item.get("name")
        socialMediaType = item.get("type")
        url = constructUrl(socialMedia, socialMediaType)
        scomUserName = "scomuser-" + str(scomuserNum) if scomuserNum is not None else None
        user_object = User(
            scomuserNum,
            user_id,
            socialMedia,
            socialMediaType,
            url,
            scomUserName,
        )
        user_objects.append(user_object)
    return (user_objects)
	

