from bs4 import BeautifulSoup
import os

def getting_parse_data(i):
	i = i.split("_")[0]
	i = i.split(" ")
	return (i[0])

def getting_scrape_data_insta_profile(htmlText):
    i = BeautifulSoup(htmlText, "html.parser")
    meta = i.find("meta", property="og:description")
    return getting_parse_data(meta.attrs['content'])


# ----------->	below code os for testing purposes	<------------

directory_path = "instagramProfilesHtmlFile"  # Replace with your actual directory path

# List all files in the directory
file_list = os.listdir(directory_path)

counter = 1

for file_name in file_list:
	file_path = os.path.join(directory_path, file_name)
    # Check if it's a file (not a directory)
	if os.path.isfile(file_path):
		with open(file_path, "r", encoding="utf-8", errors="replace") as file:
			file_content = file.read()
	print(getting_scrape_data_insta_profile(file_content))
