import tweepy
from dotenv import load_dotenv
from file_handle import FileHandle
import os

class AppConfig:
  __config = {
    "TWITTER_API_KEY": "",
    "TWITTER_API_SECRET": "",    
    "TWITTER_ACCESS_TOKEN": "",
    "TWITTER_ACCESS_SECRET": ""
  }

  @staticmethod
  def get(name):
    return AppConfig.__config[name]

  @staticmethod
  def set(name, val):
    AppConfig.__config[name] = val

  @staticmethod
  def init():
    # Load env config
    load_dotenv()
    
    AppConfig.set("TWITTER_API_KEY", os.getenv("TWITTER_API_KEY"))
    AppConfig.set("TWITTER_API_SECRET", os.getenv("TWITTER_API_SECRET"))
    AppConfig.set("TWITTER_ACCESS_TOKEN", os.getenv("TWITTER_ACCESS_TOKEN"))
    AppConfig.set("TWITTER_ACCESS_SECRET", os.getenv("TWITTER_ACCESS_SECRET"))
