from extractInstaPostData import checkUserNamePresence
from extractTiktokProfileData import strCountToInt
from emojieDictionary import replaceEmojis

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
		return (None)
