import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import sys
import time
import argparse
import string
#import config
import json

keyfile = sys.argv[1]

with open(keyfile) as f:
    content = [line.rstrip('\n') for line in f]


consumer_key = content[0]
consumer_secret = content[1]
access_token = content[2]
access_secret = content[3]

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class TweetListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweets.json', 'a') as t:
                t.write(data)
                return True
        except BaseException as e:
            print "Error at ", str(e)
        return True

    def on_error(self, status):
        print(status)
        return True

print "Script in Progress"

twitter_stream = Stream(auth, TweetListener())
twitter_stream.filter(track=['#sanfrancisco,#apple,#ucr,#riverside,#uc,#blackfriday,#thansgiving'],locations=[-122.75,36.8,-121.75,37.8])
