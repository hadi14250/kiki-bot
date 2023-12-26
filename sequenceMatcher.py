from difflib import SequenceMatcher
import emoji

# strips emojis for twitter because twitter strips emojies in html
def stripEmojis(originalContentPost):
    return ''.join(c for c in originalContentPost if not emoji.is_emoji(c))

def stripWhitespaces(inputString):
    return inputString.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")


def get_similarity_percentage(userPost, originalContentPost, type):
    if not (userPost) or not (originalContentPost):
        return ("0.0%")
    # if (type == "twitter"):
    originalContentPost = stripEmojis(originalContentPost)

    originalContentPost = stripWhitespaces(originalContentPost)
    userPost = stripWhitespaces(userPost)
    
    # Create a SequenceMatcher object
    seq_matcher = SequenceMatcher(None, userPost, originalContentPost)

    # Get the ratio of similarity (a float between 0 and 1)
    similarity_ratio = seq_matcher.ratio()

    # Convert the similarity ratio to a percentage
    similarity_percentage = similarity_ratio * 100

    return similarity_percentage