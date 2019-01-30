from twitter_stream_api import TwitterStreamAPI
from config import AppConfig

# Init AppConfig
AppConfig.init()

stream = TwitterStreamAPI()

stream.add_filters('trump', 'shutdown', 'border')

stream.start()