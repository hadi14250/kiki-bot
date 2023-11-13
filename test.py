from bs4 import BeautifulSoup
import os
from insta import getting_scrape_data_insta_profile, getting_scrape_data_insta_post
import time

# directory_path = "instagramHtmlFile"  # Replace with your actual directory path

# # List all files in the directory
# file_list = os.listdir(directory_path)

# # Loop through each file and read its content
# for file_name in file_list:
# 	file_path = os.path.join(directory_path, file_name)
#     # Check if it's a file (not a directory)
# 	if os.path.isfile(file_path):
# 		with open(file_path, "r", encoding="utf-8") as file:
# 			file_content = file.read()
# 			print("\n", file_name, "Has: {} followers\n".format(getting_scrape_data_insta_profile(file_content)["Followers"]))
# 			# print("Followers: {}".format(getting_scrape_data_insta_profile(file_content)["Followers"]))
# 			# print("Followers: {}".format(getting_scrape_data_insta_profile(file_content)["followers"]))
# 			time.sleep(0.1)
#             # Process the file content as needed
#             # print(f"Content of {file_name}:\n{file_content}\n")


fileName = "instagram_post_Abbas Ja3far.html"
if os.path.isfile(fileName):
		with open(fileName, "r", encoding="utf-8") as file:
			file_content = file.read()
		i = BeautifulSoup(file_content, "html.parser")
		# meta = i.find("meta", property="og:title")
		meta = i.find("meta", property="og:description")
		print(meta)
