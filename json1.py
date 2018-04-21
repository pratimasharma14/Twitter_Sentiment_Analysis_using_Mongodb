# encoding: utf-8

import tweepy
import json

consumer_key = 'YLTsg6saxKSLfs7BO3fUSvMsS'
consumer_secret = 'zEpcBoSK7nyLFCxsKCs3YXs7uwT4tkcQVc8M5TGw5FABpaYC3w'
access_token = '29405602-nIDqtYPLpQF6hNZ5Iq6ZcZ3U5iSIFnMuaKTC0arQi'
access_token_secret = 'XAJQ4SJR33wf3pSmGi1Eopzzj34mHVGDsDebHrq52AV41'

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Parsing 
        decoded = json.loads(data)
        #open a file to store the status objects
        file = open('stream.json', 'w')  
        #write json to file
        json.dump(decoded,file,sort_keys = True,indent = 4)
        #show progress
        print ("Writing tweets to file,CTRL+C to terminate the program")

        
        return True

    def on_error(self, status):
        print (status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = tweepy.Stream(auth, l)
    #Hashtag to stream
    stream.filter(track=["#love"])
