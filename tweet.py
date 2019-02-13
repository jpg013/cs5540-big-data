def parse_hashtags(status):
    """Takes a twitter status and parses the hashtags, returning a 
    comma-delimited string"""
    hashtags = status.entities["hashtags"]

    if hashtags is None or len(hashtags) is 0:
        return None

    return " ".join(x["text"] for x in hashtags)

def parse_urls(status):
    """Takes a twitter status and parses the urls, returning a 
    comma-delimited string"""
    urls = status.entities["urls"]
    
    if urls is None or len(urls) is 0:
        return None
    
    return " ".join(x["expanded_url"] for x in urls)

def extract_entities(status):
    return {
        "hashtags": parse_hashtags(status),
        "urls": parse_urls(status)
    }