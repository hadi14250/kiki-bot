from bs4 import BeautifulSoup
import os
import time
import re
from datetime import datetime

def extractInstagramLikeCount(input_string):
    # Check for the presence of "likes" in the input string
    if "likes" not in input_string.lower():
        return 0

    # Define a regular expression pattern to match different formats of like counts
    pattern = re.compile(r'(\d{1,3}(?:,\d{3})*(?:\.\d+)?)\s*(K|k|M|m)?', re.IGNORECASE)

    # Search for the pattern in the input string
    match = pattern.search(input_string)

    if match:
        # Extract and normalize the like count
        like_count = match.group(1).replace(',', '')
        unit = match.group(2)

        if '.' in like_count:
            # If decimal part is present, convert to integer after multiplying with the appropriate factor
            like_count = str(int(float(like_count) * (1000 if unit.lower() == 'k' else 1000000)))
        else:
            # If no decimal part, multiply with 'K' or 'M' accordingly
            if unit and unit.lower() == 'k':
                like_count = str(int(like_count) * 1000)
            elif unit and unit.lower() == 'm':
                like_count = str(int(like_count) * 1000000)

        return int(like_count)
    else:
        return 0  # Return None if there is no match

def extractInstagramUsername(input_string):
    # Define a regular expression pattern to match the username
    pattern = re.compile(r'\s*-\s*([\w_]+)\s*on', re.IGNORECASE)

    # Search for the pattern in the input string
    match = pattern.search(input_string)

    if match:
        # Extract the username
        username = match.group(1)
        return username
    else:
        return None

def extractInstagramDate(input_string):
    # Define a date format that matches the date pattern in your input string
	date_format = "%B %d, %Y"

    # Split the input string to extract the date part
	date_part = input_string.split('on')[-1].strip()
    
	# Remove the trailing colon, if present
	date_part = date_part.rstrip(':')

	try:
		# Parse the date using the specified format
		date_object = datetime.strptime(date_part, date_format).date()
		return date_object
	except ValueError:
        # Handle the case where the date cannot be parsed
		return None

# removes "username on Instagram" text from the title tag to give the raw
# text of the post.
def extractInstagramContent(input_string):
    # Find the index of "on Instagram: " in the input string
    start_index = input_string.find('on Instagram: ')
    
    if start_index != -1:
        # Extract the substring starting from the end of "on Instagram: "
        substring = input_string[start_index + len('on Instagram: '):]
        
        # Check if the substring contains quotes
        if '"' in substring:
            # Find the index of the first quote
            quote_start_index = substring.find('"')
            
            # Find the index of the second quote, starting from the position after the first quote
            quote_end_index = substring.find('"', quote_start_index + 1)
            
            # Extract the content within the quotes
            content = substring[quote_start_index + 1:quote_end_index]
            return content.strip()

    return None


#The regular expression (.*?) will capture everything up
# to the date pattern, and (\d{1,2}, \d{4}) will capture
# the date "November 5, 2023". The colon : is also included.
def formatInput(input_string):
    match = re.search(r'(.+?(\d{1,2}, \d{4}):)', input_string)

    if match:
        # If a match is found, return the formatted input
        formatted_input = match.group(1).strip()
        return formatted_input
    else:
        # If no match is found, return the original input
        return input_string.strip()

# replace "type"  with "likesCount" for likes
# or with "userName" for instagram username
# or with "postDate" for date of the post
def	extractInstaPostData(htmlResponse, type):

	soup = BeautifulSoup(htmlResponse, "html.parser")

	# extracting meta html tag with the "og:description" property
	metaDesc = soup.find("meta", property="og:description")
	metaDescContent = metaDesc.get("content") if metaDesc else ""
	formattedMetaDescContent = formatInput(metaDescContent)

	# extracting meta html tag with the "og:title" property
	metaTitle = soup.find("meta", property="og:title")
	metaTitleContent = metaTitle.get("content") if metaTitle else ""

	if (type == "userName"):
		return (extractInstagramUsername(formattedMetaDescContent))
	elif (type == "likeCount"):
		return (extractInstagramLikeCount(formattedMetaDescContent))
	elif (type == "content"):
		return (extractInstagramContent(metaTitleContent))
	elif (type == "postDate"):
		return (extractInstagramDate(formattedMetaDescContent))




# ----------->	below code os for testing purposes	<------------

# directory_path = "instagramPostsHtmlFile"  # Replace with your actual directory path

# # List all files in the directory
# file_list = os.listdir(directory_path)

# counter = 1

# # Loop through each file and read its content
# for file_name in file_list:
# 	file_path = os.path.join(directory_path, file_name)
#     # Check if it's a file (not a directory)
# 	if os.path.isfile(file_path):
# 		with open(file_path, "r", encoding="utf-8", errors="replace") as file:
# 			file_content = file.read()
# 			print("----------> ((->{}<-))\nusername".format(counter),
# 				"\"[[[[[[{}]]]]]]\"".format(extractInstaPostData(file_content, "userName")),
#                 "has:", 
#                 extractInstaPostData(file_content, "likeCount"),
#                 "likes",
#                 "on Date",
#                 extractInstaPostData(file_content, "postDate"),
#                 f"-----> [[[[[[{extractInstaPostData(file_content, 'content')}]]]]]] <-----",
#                 "\n<----------")
# 	counter += 1
            

