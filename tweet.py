def parse_status_hashtags(status):
    """Takes a twitter status and parses the hashtags, returning a 
    comma-delimited string"""
    hashtags = status.entities["hashtags"]

    if hashtags is None or len(hashtags) == 0:
        return None

    return ", ".join(x["text"] for x in hashtags)

def parse_status_urls(status):
    """Takes a twitter status and parses the urls, returning a 
    comma-delimited string"""
    urls = status.entities["urls"]
    
    if urls is None or len(urls) == 0:
        return None

    return ", ".join(x["url"] for x in urls)