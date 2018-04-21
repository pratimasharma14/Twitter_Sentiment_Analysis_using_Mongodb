import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.tutorial


import tweepy

consumer_key = 'YLTsg6saxKSLfs7BO3fUSvMsS'
consumer_secret = 'zEpcBoSK7nyLFCxsKCs3YXs7uwT4tkcQVc8M5TGw5FABpaYC3w'
access_token = '29405602-nIDqtYPLpQF6hNZ5Iq6ZcZ3U5iSIFnMuaKTC0arQi'
access_secret = 'XAJQ4SJR33wf3pSmGi1Eopzzj34mHVGDsDebHrq52AV41'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
public_tweets = api.home_timeline()
import sys

for tweet in public_tweets:
    #result=db.employee.insert_one({'name':'ranjan kumar','roll':'1009','age':'41'})
    db.tweet.insert({'id':1001,'name':tweet.text})
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    #print(x.translate(non_bmp_map))
    print(str(tweet).translate(non_bmp_map))
    #print(tweet.text)




#print('This works! \U0001F44D')
#print('This works! \U0001F44D'.translate(non_bmp_map))



