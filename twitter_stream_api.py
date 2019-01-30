import tweepy
from file_handle import FileHandle, FileModes
from config import AppConfig
import tweet
import os

#auth = tweepy.OAuthHandler(AppConfig.get("TWITTER_API_KEY"), AppConfig.get("TWITTER_API_SECRET"))
#auth.set_access_token(AppConfig.get("TWITTER_ACCESS_TOKEN"), AppConfig.get("TWITTER_ACCESS_SECRET"))

#api = tweepy.API(auth)

#override tweepy.StreamListener to add logic to on_status
"""
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        hashtags = status.entities["hashtags"]
        urls = status.entities["urls"]

        if len(hashtags) > 0:
            s = " ".join(x["text"] for x in hashtags)
            print(s)
"""
            # hashtag_file.write(s + "\n")

            # str(x) for x in list]
            # s = " ".join(hashtags)
            # print(s)
            # hashtag_file.write("test")
            # s = " ".join(hashtags)
            # print(s)
            #hashtag_file.write("test")

        #if len(urls) > 0:
         #   print(urls)
            # s = " ".join(urls)
            # print(s)
            #hashtag_file.write("test")


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
    
    def __init__(self):
        # Call super init
        super().__init__()

        self.stream = tweepy.Stream(
            auth = self.api.auth, 
            listener=HashtagUrlStreamListener()
        )
    
    def add_filters(self, *filters):
        self.filters = self.filters + list(filters)

    def start(self):
        self.stream.filter(track=self.filters)

class HashtagUrlStreamListener(tweepy.StreamListener):
    """StreamListener class that parses out hashtags/urls from 
    each status and stores them in a file"""
    
    def __init__(self, dirname=os.path.join(os.path.dirname(__file__), 'data')):
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
        
    def on_status(self, status):    
        hashtags = tweet.parse_status_hashtags(status)
        urls = tweet.parse_status_urls(status)

        self.hashtag_file.write(hashtags+"\n") if hashtags is not None else None
        self.url_file.write(urls+"\n") if urls is not None else None
            