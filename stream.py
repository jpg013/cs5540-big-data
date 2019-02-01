from twitter_stream_api import TwitterStreamAPI
from config import AppConfig
import time

# Init AppConfig
AppConfig.init()

stream = TwitterStreamAPI(limit=100)

stream.add_filters("trump").start()
