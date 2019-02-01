import tweepy
from file_handle import FileHandle, FileModes
from config import AppConfig
import tweet
import os
import math
test = math.inf

class TwitterAPI():
    """Twitter API is a wrapper calss around the tweepy api."""

    def __init__(self): 
        auth = tweepy.OAuthHandler(
            AppConfig.get("TWITTER_API_KEY"), 
            AppConfig.get("TWITTER_API_SECRET")
        )

        auth.set_access_token(
            AppConfig.get("TWITTER_ACCESS_TOKEN"), 
            AppConfig.get("TWITTER_ACCESS_SECRET")
        )

        self.api = tweepy.API(auth)

class TwitterStreamAPI(TwitterAPI):
    filters=[]
    
    def __init__(self, limit=math.inf):
        # Call super init
        super().__init__()

        self.stream = tweepy.Stream(
            auth = self.api.auth, 
            listener=StatusStreamListener(limit)
        )

    def add_filters(self, *filters):
        self.filters = self.filters + list(filters)
        
        return self

    def start(self):
        self.stream.filter(track=self.filters, is_async=True)

    def stop(self):
        print("calling disconnect")
        self.stream.disconnect()

class StatusStreamListener(tweepy.StreamListener):
    """StatusStreamListener class that parses twitter stream statuses"""
    
    def __init__(
        self, 
        limit=math.inf,
        dirname=os.path.join(os.path.dirname(__file__), "input")
    ):
        # Call super init
        super().__init__()
        
        self.hashtag_file = FileHandle(
            file_path=os.path.join(dirname, 'hashtags.txt'),
            mode=FileModes.APPEND
        )

        self.url_file = FileHandle(
            file_path=os.path.join(dirname, 'urls.txt'),
            mode=FileModes.APPEND
        )

        self.limit = limit
        self.count = 0
        
    def on_status(self, status):    
        """Called whenever there is a new status from twitter stream"""
        hashtags = tweet.parse_status_hashtags(status)
        urls = tweet.parse_status_urls(status)

        self.hashtag_file.write(hashtags+"\n") if hashtags is not None else None
        self.url_file.write(urls+"\n") if urls is not None else None

        self.count += 1
        # If we have exceeded the limit then return False to stop the stream
        if self.count >= self.limit:
            return False
        
    def on_error(self, status_code):
        if status_code == 420:
            print("we are receiving a 420 error")
            #returning False in on_data disconnects the stream
            return False
            