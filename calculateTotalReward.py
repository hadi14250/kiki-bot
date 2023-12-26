from extractInstaPostData import checkUserNamePresence

def calcPaymentFollowers(followers, contentSimilarity):
    followers = int(followers) if followers else 0  # Convert to int if followers is not None
    contentSimilarity = int(contentSimilarity) if str(contentSimilarity).replace('.', '').isdigit() else 0  # Convert to int if contentSimilarity is a digit
    
    if (contentSimilarity < 85) or ((followers) and (followers < 300)):
        return (0)
    if not (followers):
        return (10)
    if (followers >= 300) and (followers <= 1000):
        return (10)
    elif (followers >= 1000) and (followers <= 5000):
        return (25)
    elif (followers >= 5000) and (followers <= 10000):
        return (40)
    elif (followers >= 10000) and (followers <= 20000):
        return (75)
    elif (followers >= 20000) and (followers <= 50000):
        return (125)
    elif (followers >= 50000) and (followers <= 150000):
        return (175)
    elif (followers >= 150000) and (followers <= 250000):
        return (250)
    elif (followers >= 250000) and (followers <= 500000):
        return (500)
    elif (followers >= 500000) and (followers <= 100000000):
        return (10000)
    return (0)
    
    

def calculateTotalReward(user):
    tiktokPayment = 0
    twitterPayment = 0
    totalPayment = 0

    if (checkUserNamePresence(user.scomUserName, user.instaPost.postText) == None):
        instaPayment = 0
    else:
        instaPayment = calcPaymentFollowers(user.instaProfile.followers, user.instaPost.contentSimilarity)
    if (checkUserNamePresence(user.scomUserName, user.tiktokPost.postText) == None):
        tiktokPayment = 0
    else:
        tiktokPayment = calcPaymentFollowers(user.tiktokProfile.followers, user.tiktokPost.contentSimilarity)
    if (checkUserNamePresence(user.scomUserName, user.tweet.postText) == None):
        twitterPayment = 0
    else:
        twitterPayment = calcPaymentFollowers(user.twitterProfile.followers, user.tweet.contentSimilarity)

    totalPayment = instaPayment + tiktokPayment + twitterPayment
    return (totalPayment)