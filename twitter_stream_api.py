import tweepy
from config import AppConfig
import math
from progress_bar import progress_bar
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
        self.update_progress()

    def update_progress(self):
        progress_bar(iteration=self.chunks, total=self.limit, prefix = 'Progress:', suffix = 'Complete', length = 50)

    def on_status(self, chunk):
        self.chunks += 1

        # Publish the status to all listeners
        self.publish_status(chunk)

        # Update the progress bar
        self.update_progress()
        
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