from twitter_stream_api import TwitterStreamAPI
from config import AppConfig
import time

# Init AppConfig
AppConfig.init()

stream = TwitterStreamAPI()

stream.add_filters("super bowl")

stream.start()
