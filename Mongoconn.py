import pymongo

from pymongo import MongoClient

connection = MongoClient('localhost',27017)
db = connection.tutorial


import tweepy

consumer_key = 'NHUyCpBlgv1rG3RE4rM8SaQAU'
consumer_secret = 'EntHlXvgw1Z79WBMfrEXcpMw3IM6gxTvZ440IGIsZVJlnaJSil'
access_token = '390032709-6XbDnfeZkRsHeVCklMbJdCK2S6s4oKie8KFViDJ3'
access_secret = 'nJmVsyZEYx8kB3AM35fzZtUce5j9UvH1H3le8uBNajjHt'


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



