from emojieDictionary import replaceEmojis

def getTweet(soupHtml):
    if not (soupHtml):
        return (None)
    tweet_text_div = soupHtml.find('div', {'data-testid': 'tweetText'})
    if tweet_text_div:
        # Find all spans that contain text and don't have images
        text_spans = [span.get_text(strip=True) for span in tweet_text_div.find_all('span') if span.get_text(strip=True) and not span.find('img')]
        
        # Join the text spans with spaces
        tweet_text = ''.join(text_spans)
        return (replaceEmojis(tweet_text))

