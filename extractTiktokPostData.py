from extractInstaPostData import checkUserNamePresence
from extractTiktokProfileData import strCountToInt
from emojieDictionary import replaceEmojis
from datetime import datetime, timedelta

def getTiktokLikes(input_text):
	# Find the index of "Likes"
	likes_index = input_text.find('Likes')

	if likes_index != -1:
		# Extract the substring before "Likes" and remove leading/trailing whitespaces
		likes_text = input_text[:likes_index].strip()

		# Find the last space character in the extracted text
		last_space_index = likes_text.rfind(' ')

		if last_space_index != -1:
			# Consider the substring after the last space as the number of likes
			likeInt = strCountToInt(likes_text[last_space_index + 1:].strip())
			return likeInt
		else:
			# If no space is found, the entire extracted text might be the number of likes
			likeInt = strCountToInt(likes_text)
			return likeInt

	return None

def extractTextBeforeQuotes(input_string):
    # Find the index of the first quote character
    quote_index = input_string.find('"')

    # Check if a quote is found
    if quote_index != -1:
        # Extract the text before the quote
        extracted_text = input_string[:quote_index].strip()
        return extracted_text
    else:
        # If no quote is found, return the original string
        return input_string.strip()

def	extractTiktokDescription(soupHtml):
	try:
		scriptTag = soupHtml.find("script", id="__UNIVERSAL_DATA_FOR_REHYDRATION__")
		if not (scriptTag):
			return (None)
		inputText = scriptTag.contents[0][:18000]
		startIndex = inputText.find('"description":"')

		if startIndex != -1:
			# Move the index to the end of the first marker
			startIndex += len('"description":"')

			# Find the index of the second marker
			endIndex = inputText.find('","canonicalHref":', startIndex)

			if endIndex != -1:
				# Extract the text between the markers
				extractedText = inputText[startIndex:endIndex]
				return (extractedText)
			else:
				return None
		else:
			return None
	except:
		return (None)

def extractTiktokPostContent(input_string):
    # Find the indices of the first and last quote characters
    start_quote_index = input_string.find('"')
    end_quote_index = input_string.rfind('"')

    # Check if both quote characters are found
    if start_quote_index != -1 and end_quote_index != -1:
        # Extract the text between the quotes
        extracted_text = input_string[start_quote_index + 1:end_quote_index].strip()
        return extracted_text
    else:
        # If one or both quote characters are not found, return an empty string
        return None

def parseTiktokDate(dateText):

    if dateText is None:
        return None
    # Get the current date
    current_date = datetime.now()

    if '-' in dateText:
        # If the date format is MM-DD
        date_obj = datetime.strptime(dateText, "%m-%d").replace(year=current_date.year)
    elif 'd ago' in dateText:
        # If the date format is X days ago
        days_ago = int(dateText.split('d ago')[0])
        date_obj = current_date - timedelta(days=days_ago)
    else:
        # Handle other formats if needed
        date_obj = None

    return date_obj.date() if date_obj else None

def findTiktokDate(soupHtml):
	# Find the span element containing the date
	dateSpan = soupHtml.select_one('span[data-e2e="browser-nickname"] span:last-child')

	# Extract the date text
	date_text = dateSpan.text if dateSpan else None
	return (parseTiktokDate(date_text))

def	extractTiktokPostData(soupHtml, type, csvUserName):
		extractedText = extractTiktokDescription(soupHtml)
		if not (extractedText):
			return (None)
		if (type == "likeCount"):
			return (getTiktokLikes(extractedText))
		elif (type == "userName"):
			tiktokHandleText = extractTextBeforeQuotes(extractedText)
			return (checkUserNamePresence(csvUserName, tiktokHandleText))
		elif (type == "content"):
			tiktokText = extractTiktokPostContent(extractedText)
			if not (tiktokText):
				return ("NO_CONTENT")
			return (replaceEmojis(tiktokText))
		elif (type == "postDate"):
			return (findTiktokDate(soupHtml))
		return (None)
