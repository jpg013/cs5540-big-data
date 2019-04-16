import re
from textblob import TextBlob

def clean_text(text):
    '''
    Utility function to clean text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", text).split())

def get_sentiment(text):
    '''
    Utility function to classsssify sentiment of passed text
    using textblob's sentiment method
    '''
    # create TextBlob object of passed text
    analysis = TextBlob(clean_text(text))

    # format sentiment
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity == 0:
        return "neutral"
    else:
        return "negative"

def parse_hashtags(status):
    """Takes a twitter status and parses the hashtags, returning a 
    comma-delimited string"""
    hashtags = status["entities"]["hashtags"]

    if hashtags is None or len(hashtags) is 0:
        return None

    return " ".join(x["text"] for x in hashtags)

def parse_urls(status):
    """Takes a twitter status and parses the urls, returning a 
    comma-delimited string"""
    urls = status["entities"]["urls"]
    
    if urls is None or len(urls) is 0:
        return None
    
    return " ".join(x["expanded_url"] for x in urls)

def transform_status(status):
    json = status._json    
    
    return {
        "created_at": json["created_at"],
        "text": json["text"],
        "sentiment": get_sentiment(json["text"]),
        "name": json["user"]["name"],
        "screen_name": json["user"]["screen_name"],
        "location": json["user"]["location"],
        "followers_count": json["user"]["followers_count"],
        "friends_count": json["user"]["friends_count"],
        "statuses_count": json["user"]["statuses_count"],
        "favourites_count": json["user"]["favourites_count"],
        "user_created_at": json["user"]["created_at"],
        "get": json["geo"],
        "coordinates": json["coordinates"],
        "quote_count": json["quote_count"],
        "reply_count": json["reply_count"],
        "retweet_count": json["retweet_count"],
        "favorite_count": json["favorite_count"],
        "hashtags": json["entities"]["hashtags"],
        "hashtags_string": parse_hashtags(json),
        "urls": json["entities"]["urls"],
        "urls_string": parse_urls(json)
    }