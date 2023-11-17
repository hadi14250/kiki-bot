import json
# print("Truncated JSON Content:\n----->\n{}\n<-----\n".format(json_content[:1500]))
from extractTiktokProfileData import strCountToInt

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

def	extractTiktokLikes(scriptTag):
	try:
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
				return (getTiktokLikes(extractedText))
			else:
				return None
		else:
			return None
	except:
		return (None)


def	extractTiktokPostData(soupHtml, type):
    # Find the script tag by id
	try:
		scriptTag = soupHtml.find("script", id="__UNIVERSAL_DATA_FOR_REHYDRATION__")
		# print("Original\n--->{}\n\n".format(scriptTag.contents[0][:18000]))
		if (type == "likeCount"):
			return (extractTiktokLikes(scriptTag))
	except:
		return(None)
