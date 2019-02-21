import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener 


consumer_key = 'r8BqAgfNYXSVnlElPuAlfRCVT'
consumer_secret ='W2tW9j6SmKG59qn2xMwP6ojhBe6g3DzKk4CmmRQtOl3VE1RxzA'
access_token = '1094675114891845632-TEn7tI11ZEyshO4pkP5W7dw6KySWHJ'
access_secret = '8T1esyezmrUcGmncQ9X6eGN51lYodG1cuJjPm4tIi0pRN'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
 
class MyListener(StreamListener):
 
    def on_data(self, data):
       #print(data)
       newFile = open('tweets_output.txt','a')
       newFile.write(data)
       newFile.write('\n')
       newFile.close()  
       return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['Trump'])

