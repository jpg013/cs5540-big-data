from twitter_stream_api import TwitterStream
from config import AppConfig
from file_handle import FileHandle, FileModes
import os
import json
from transform_status import transform_status

file_name="tweets.json"

# Init AppConfig
AppConfig.init()

stream = TwitterStream(limit=100)

data_dir=os.path.join(os.path.dirname(__file__), "json")

json_file = FileHandle(os.path.join(data_dir, file_name), mode=FileModes.APPEND)

def on_status(status):
    json_file.write(json.dumps(transform_status(status)))

stream.add_listener(on_status)
# Bounding box I drew for Kansas City using 
# https://boundingbox.klokantech.com/

KANSAS_CITY_GEO_BOX = [-95.1196, 38.7307, -93.9914, 39.3881] # Kansas City Metro area

#stream.add_location_filter(location_filter)
stream.add_track_filter("trump")

stream.start()

