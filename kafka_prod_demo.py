#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 29 15:04:38 2021

@author: rita
"""
import tweepy
import time
from kafka import KafkaProducer
import json
from bson import json_util

# Twitter API's Key

access_token = '811205561643515904-89kdYOal4whT4hoyzg5KMqpDu8Mx1fK'
access_token_secret = 'zMVNpFtHI9fVvtuP0LnomptaHhEQ7aKEWGwjV3iW504Zo'
consumer_key = 'obQRWkMGxeM5HTgigVM6uK91V'
consumer_secret = 'BTyRtsvKZLrWEOeOaF3nYSNd74i0LkRyNNumfn33a5xPKki8B1'

# Creating authentication object

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Setting your access token and secret

auth.set_access_token(access_token, access_token_secret)

# Creating the API object by passing in auth information

api = tweepy.API(auth)

# Formatting date and time

from datetime import datetime

def normalize_timestamp(time):
    mytime = datetime.strptime(time, "%Y-%m-%d %H:%M:%S")
    return mytime.strftime("%Y-%m-%d %H:%M:%S")

# KafkaProducer

producer = KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0,11,5))
topic_name = 'trump'

# Get data from Twitter

def get_twitter_data():
    res = api.search_tweets('#omicron')
    for i in res:
        date = str(i.created_at)
        
        hashtags = i.entities['hashtags']
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])
        
        '''record = ""
        record += 'Created_date:'+str(date[:16])
        record += '\n'
        record += 'Username:'+str(i.user.screen_name)
        record += '\n'
        record += 'User_location:'+str(i.user.location)
        record += '\n'
        record += 'Hashtags:' +str(hashtext)
        record += '\n'
        record += 'Text:'+str(i.text[:100])
        record += '\n\n'
        '''
        
        record = dict()
        record['Created_date']=str(date[:16])
        record['Username']=str(i.user.screen_name)
        record['User_location']=str(i.user.location)
        record['Hashtags']=str(hashtext)
        record['Text']=str(i.text[:100])
        
        

        producer.send(topic_name, json.dumps(record, ).encode('utf-8'))
        

def periodic_work(interval):
    while True:
        get_twitter_data()
        # interval should be an integer, the number of seconds to wait
        time.sleep(interval)
        
periodic_work(60*0.1) # get data every couple of minutes


