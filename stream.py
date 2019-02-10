from twitter_stream_api import TwitterStream
from config import AppConfig
import tweet
import time

# Init AppConfig
AppConfig.init()

stream = TwitterStream(limit=100)

def on_status(status):
    print(tweet.extract_entities(status))

stream.add_listener(on_status)
# Bounding box I drew for Kansas City using 
# https://boundingbox.klokantech.com/

location_filter = [-95.1196, 38.7307, -93.9914, 39.3881] # Kansas City Metro area

# stream.add_location_filter(location_filter)
stream.add_track_filter("trump")
stream.start()

