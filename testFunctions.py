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
    stringToPrint = "\n\nInsta Username: {} has {} followers, Profile job_id is: {}, Post job_id is: {}  content is \n----------->\n{}\n<-----------\ncontent similarity: {}\n\nScom Username: {}, Total Payment: {}$\n\n".format(
        user.instaPost.excractedUserName, user.instaProfile.followers,
        user.instaProfile.proxyJobID, user.instaPost.proxyJobID, user.instaPost.postText, user.instaPost.contentSimilarity, user.scomUserName, user.totalPayment)
    printContentToFile(stringToPrint, fileName, dirName)

    stringToPrint = "Tiktok Username: {} has {} followers, Profile job_id is: {}, Post job_id is: {}  content is \n----------->\n{}\n<-----------\ncontent similarity: {}\n\nScom Username: {}, Total Payment: {}$\n\n".format(
        user.tiktokPost.excractedUserName, user.tiktokProfile.followers,
        user.tiktokProfile.proxyJobID, user.tiktokPost.proxyJobID, user.tiktokPost.postText, user.tiktokPost.contentSimilarity, user.scomUserName, user.totalPayment)
    printContentToFile(stringToPrint, fileName, dirName)

    stringToPrint = "Twitter Username: {} has {} followers, Profile job_id is: {} content is \n-------------->\n{}\n<------------\ncontent similarity: {}\n\nScom Username: {}, Total Payment: {}$\n\n".format(
        user.twitterProfile.csvUserName, user.twitterProfile.followers,
        user.twitterProfile.proxyJobID, user.tweet.postText, user.tweet.contentSimilarity, user.scomUserName, user.totalPayment)
    printContentToFile(stringToPrint, fileName, dirName)