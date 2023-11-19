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

# ----------->	below code os for testing purposes	<------------

# directory_path = "instagramProfilesHtmlFile"  # Replace with your actual directory path

# # List all files in the directory
# file_list = os.listdir(directory_path)

# counter = 1

# for file_name in file_list:
# 	file_path = os.path.join(directory_path, file_name)
#     # Check if it's a file (not a directory)
# 	if os.path.isfile(file_path):
# 		with open(file_path, "r", encoding="utf-8", errors="replace") as file:
# 			file_content = file.read()
# 	print(getInstaFollowers(file_content))
