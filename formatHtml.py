import re
from extractInstaProfileData import getInstaFollowers

def formatHtml(rawHtml):
	if not (rawHtml):
		return (None)
	rawHtml = rawHtml.replace("\\n", "\n").replace("\\", "")
	start_pattern = re.compile(r'<html[^>]*>')
	end_pattern = re.compile(r'</html>')
	start_match = start_pattern.search(rawHtml)
	end_match = end_pattern.search(rawHtml)

	if start_match and end_match:
		start_pos = start_match.end()
		end_pos = end_match.start()
		trimmed_html = rawHtml[start_pos:end_pos].strip()
	else:
		trimmed_html = rawHtml  # Fallback if HTML tags are not found
	return trimmed_html

def	printInstagramInfo(htmlText):
	if __name__ == "__main__":
		try:
			data = getInstaFollowers(htmlText)
			print(f"Hadi has", data["Followers"], data["followers"])
			print(f"Hadi has", data["Following"], data["following"])
			print(f"Hadi has", data["Posts"], data["posts"])
		except Exception as e:
			print("Failed to print Instagram Info: {}".format(e))