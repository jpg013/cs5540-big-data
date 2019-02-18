from twitter_stream_api import TwitterStream
from config import AppConfig
import tweet
from file_handle import FileHandle, FileModes
import os

# Init AppConfig
AppConfig.init()

stream = TwitterStream(limit=100)

log_path=os.path.join(os.path.dirname(__file__), "logs", "stream-output.log")

log_file = FileHandle(log_path, mode=FileModes.APPEND)

def on_status(status):
    data = tweet.extract_entities(status)
    
    if data["hashtags"]:
        log_file.write(data["hashtags"] + "\n")    

    if data["urls"]:
        log_file.write(data["urls"] + "\n")

stream.add_listener(on_status)
# Bounding box I drew for Kansas City using 
# https://boundingbox.klokantech.com/

KANSAS_CITY_GEO_BOX = [-95.1196, 38.7307, -93.9914, 39.3881] # Kansas City Metro area

#stream.add_location_filter(location_filter)
stream.add_track_filter("trump")
stream.start()

