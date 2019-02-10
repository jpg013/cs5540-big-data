import tweepy
from file_handle import FileHandle, FileModes
from config import AppConfig
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

class TwitterStream(TwitterAPI, tweepy.StreamListener):
    """TwitterStream inherits from TwitterAPI and tweepy StreamListenr"""
    filters=[]
    
    def __init__(self, limit=math.inf):
        # Call super init
        super().__init__()

        self.stream = tweepy.Stream(
            auth = self.api.auth, 
            listener=self
        )

        self.is_streaming = False
        self.listeners = []
        self.chunks = 0
        self.limit = limit
        self.filters = {
            "locations": [],
            "track": []
        }

    def on_status(self, chunk):
        self.chunks += 1

        # Publish the status to all listeners
        self.publish_status(chunk)
        
        # If we have exceeded the limit then return False to stop the stream
        if self.chunks >= self.limit:
            return False

    def add_location_filter(self, coords):
        self.filters["locations"] = self.filters["locations"] + coords
        
    def add_track_filter(self, term):
        self.filters["track"].append(term)

    def publish_status(self, status):
        for func in self.listeners:
            func(status)

    def add_listener(self, func):
        """ Adds a callback to the listeners array if it does not already exist"""
        if func in self.listeners or not callable(func):
            return
        
        self.listeners.append(func)

    def start(self):
        if self.is_streaming is True:
            return
        print(self.filters)
        self.is_streaming = True
        self.stream.filter(
            locations=self.filters["locations"], 
            track=self.filters["track"],
            is_async=True
        )

    def stop(self):
        if not self.is_streaming:
            return
        
        self.stream.disconnect()
        self.is_streaming = False

    def on_error(self, status_code):
        if status_code == 420:
            print("we are receiving a 420 error")
            #returning False in on_data disconnects the stream
            return False

class StatusStreamListener(tweepy.StreamListener):
    """StatusStreamListener class that parses twitter stream statuses"""
    
    def __init__(
        self, 
        limit=math.inf,
        # dirname=os.path.join(os.path.dirname(__file__), "input"),
        # on_status
    ):
        # Call super init
        super().__init__()
        
        """
        self.hashtag_file = FileHandle(
            file_path=os.path.join(dirname, 'hashtags.txt'),
            mode=FileModes.APPEND
        )

        hashtags = tweet.parse_status_hashtags(status)
        urls = tweet.parse_status_urls(status)

        self.hashtag_file.write(hashtags+"\n") if hashtags is not None else None
        self.url_file.write(urls+"\n") if urls is not None else None

        self.url_file = FileHandle(
            file_path=os.path.join(dirname, 'urls.txt'),
            mode=FileModes.APPEND
        )
        """