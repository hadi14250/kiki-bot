
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

def	getTiktokFollowers(soupHtml):
	# extracting meta html tag with the "og:description" property
	try:
		metaDesc = soupHtml.find("meta", property="og:description")
		metaDescContent = metaDesc.get("content") if metaDesc else ""
		return (extract_followers_count(metaDescContent))
	except:
		return (None)

