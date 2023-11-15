import os

def printHtml(htmlText, filename, dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    filename = os.path.join(dirName, filename)

    with open(filename, 'w', encoding='utf-8', errors="replace") as f:
        f.write(htmlText)


def printContentToFile(content, filename, dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

    filename = os.path.join(dirName, filename)

    with open(filename, 'a', encoding='utf-8', errors="replace") as f:
        f.write(content)

def	printUserInfo(user, fileName, dirName):
	stringToPrint = "Insta Username: {} has {} followers, on their {} post he has {} likes. content is \n----------->\n{}\n<-----------\n\n\n".format(
          user.instaProfile.csvUserName, user.instaProfile.followers,
        	user.instaPost.postDate, user.instaPost.postLike, user.instaPost.postText)

	printContentToFile(stringToPrint, fileName, dirName)
	stringToPrint = "Tiktok Username: {} has {} followers and thier post has: {} likes\n\n\n".format(
          user.tiktokProfile.csvUserName, user.tiktokProfile.followers, user.tiktokPost.postLike)
	printContentToFile(stringToPrint, fileName, dirName)