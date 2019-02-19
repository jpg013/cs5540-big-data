from twitter_stream_api import TwitterStream
from config import AppConfig
import tweet
from file_handle import FileHandle, FileModes
import os

# Init AppConfig
AppConfig.init()

stream = TwitterStream(limit=100000)

log_dir=os.path.join(os.path.dirname(__file__), "logs")

url_log = FileHandle(os.path.join(log_dir, "url.log"), mode=FileModes.APPEND)

hashtag_log = FileHandle(os.path.join(log_dir, "hashtag.log"), mode=FileModes.APPEND)

def on_status(status):
    data = tweet.extract_entities(status)
    
    if data["hashtags"]:
        hashtag_log.write(data["hashtags"] + "\n")    

    if data["urls"]:
        url_log.write(data["urls"] + "\n")

stream.add_listener(on_status)
# Bounding box I drew for Kansas City using 
# https://boundingbox.klokantech.com/

KANSAS_CITY_GEO_BOX = [-95.1196, 38.7307, -93.9914, 39.3881] # Kansas City Metro area

#stream.add_location_filter(location_filter)
stream.add_track_filter("trump")
stream.start()

