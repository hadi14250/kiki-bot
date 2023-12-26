from constructUrls import constructUrl
from findProxyJobID import findProxyJobID
from formatHtml import formatHtml
from bs4 import BeautifulSoup

class Post:
	def __init__(self, scomuserNum, id, socialMedia, socialMediaType, url, scomUserName, followers, instaStory, campaing):
		self.scomuserNum		    = scomuserNum
		self.id		            = id
		self.socialMedia	    = socialMedia
		self.socialMediaType    = socialMediaType
		self.scomUserName       = scomUserName
		self.url                = url
		self.followers          = followers
		self.instaStory         = instaStory
		self.campaing           = campaing
		self.validated          = False
		self.response			= None
		self.html				= None
		self.soupHtml			= None
		self.proxyJobID         = None
		self.excractedUserName	= None
		self.postText			= None
		self.payment			= 0
		self.contentSimilarity = 0


	def	formatHtmlResponse(self, response):
		self.proxyJobID = findProxyJobID(response.text, "job_id")
		self.response = response
		self.html = formatHtml(response.text)
		if (self.html):
			self.soupHtml = BeautifulSoup(self.html, "html.parser")

user_objects = []
def parsePostsGetRequest(response_json):
    for item in response_json:
        scomuserNum = item.get("scomuser")
        user_id = item.get("id")
        socialMedia = item.get("name")
        socialMediaType = item.get("type")
        url = item.get("url")
        followers = item.get("followers")
        instaStory = item.get("instaStory")
        campaing = item.get("campaing")
        scomUserName = "scomuser-" + str(scomuserNum) if scomuserNum is not None else None
        user_object = Post(
            scomuserNum,
            user_id,
            socialMedia,
            socialMediaType,
            url,
            scomUserName,
			followers,
			instaStory,
			campaing
        )
        user_objects.append(user_object)
    return (user_objects)


