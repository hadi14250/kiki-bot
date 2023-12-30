from extractTiktokProfileData import strCountToInt

def getting_parse_data(i):
	i = i.split("_")[0]
	i = i.split(" ")
	return (strCountToInt(i[0]))

def getInstaFollowers(soupHtml):
    if not soupHtml:
        return None
    
    meta = soupHtml.find("meta", property="og:description")
    
    if meta and 'content' in meta.attrs:
        return getting_parse_data(meta.attrs['content'])
    else:
        return None
