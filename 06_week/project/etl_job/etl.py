
"""Twe following script is meant for being used for the TWITTER API-V2.
The least tweepy version to use is 4.01"""

import pandas as pd
import re
import logging
import pymongo
from sqlalchemy import create_engine
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
import pyjokes
import requests

time.sleep(2)

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use withing the MongoDB server
db = client.twitter


pg = create_engine('postgresql://postgres:titanic99@postgresdb:5432/twitter', echo=True)

pg.execute('''
    DROP TABLE IF EXISTS tweets;
    CREATE TABLE tweets (
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

analyser = SentimentIntensityAnalyzer()

mentions_regex= '@[A-Za-z0-9]+'
url_regex='https?:\/\/\S+' #this will not catch all possible URLs
hashtag_regex= '#'
rt_regex= 'RT\s'

def clean_tweets(tweet):
    tweet = re.sub(mentions_regex, '', tweet)  #removes @mentions
    tweet = re.sub(hashtag_regex, '', tweet) #removes hashtag symbol
    tweet = re.sub(rt_regex, '', tweet) #removes RT to announce retweet
    tweet = re.sub(url_regex, '', tweet) #removes most URLs
    
    return tweet

docs = db.tweets.find()
for doc in docs:
    text = doc['text']
    text = clean_tweets(text)
    sentiment = pd.Series(analyser.polarity_scores(text))
    sentiment = sentiment['compound']
    
    query = "INSERT INTO tweets VALUES (%s, %s);"
    pg.execute(query, (text, sentiment))
    # pg.execute(query2)
    # print(text)

tweets_query = pg.execute('''
    SELECT *
    FROM tweets
;
''')

df = pd.DataFrame(tweets_query, columns = ['text', 'compound'])
# print(df)

# data = pd.DataFrame(pg.execute(query, (text, sentiment)))

webhook_url = "https://hooks.slack.com/services/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"

tweet = 0
# while tweet < 1:
# sentiment_list = []

sentiment = 'Negative'
# if df['compound'][0] < 0:
    


tweet_n_score = 'Tweet:\n' + df['text'][0]+'\n\n' + 'Compound Score:\n\n' + str(df['compound'][0]) + '\n\n' + 'Sentiment Score indicates:\n' + sentiment   
    # for tweet in df['text']:
data = {'text': tweet_n_score}
# 'compound_score':str(df['compound'][0])}
requests.post(url=webhook_url, json = data)
tweet += 1