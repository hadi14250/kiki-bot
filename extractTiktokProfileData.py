import json

# converts the number of likes or followers to an int
def strCountToInt(str_count):
    # Remove commas from the string
    str_count = str_count.replace(',', '')

    # Convert the string to an integer, handling 'M' for millions and 'K' for thousands
    followers_count_multiplier = 1
    if 'm' in str_count.lower():
        followers_count_multiplier = 1_000_000
    elif 'k' in str_count.lower():
        followers_count_multiplier = 1_000

    # Extract the numeric part and convert to an integer
    numeric_part = str_count.rstrip('MmKk')
    followers_count = int(float(numeric_part) * followers_count_multiplier)

    return followers_count


def extract_followers_count(input_string):
	# Split the input string by spaces
	if not (input_string):
		return (None)
	words = input_string.split()

	# Look for the index of "Followers."
	followers_index = words.index("Followers.")

	# Get the number of followers which is just before "Followers."
	followers_count_str = words[followers_index - 1]
	return (strCountToInt(followers_count_str))

def findFollowersUsingHtml(htmlText):
	if not (htmlText):
		return (None)
	startIndex = htmlText.find('"stats":{')
	if not (startIndex):
		return (None)
	endIndex = htmlText.find('}', startIndex) + 1
	statsJson = htmlText[startIndex:endIndex]
	followerCountIndex = statsJson.find('"followerCount":')
	if not (followerCountIndex):
		return (None)
	startIndex = statsJson.find(':', followerCountIndex) + 1
	if not (startIndex):
		return (None)
	endIndex = statsJson.find(',', startIndex)
	if not (endIndex):
		return (None)
	followerCount = statsJson[startIndex:endIndex].strip()
	if followerCount.isdigit():
		return (int(followerCount))
	else:
		return (None)

def	getTiktokFollowers(soupHtml, htmlText):
	if not (soupHtml) or not (htmlText):
		return (None)
	# extracting meta html tag with the "og:description" property
	try:
		metaDesc = soupHtml.find("meta", property="og:description")
		metaDescContent = metaDesc.get("content") if metaDesc else ""
		tiktokFollowers = extract_followers_count(metaDescContent)
		if not (tiktokFollowers):
			tiktokFollowers = findFollowersUsingHtml(htmlText)
		return (tiktokFollowers)
	except:
		return (None)

