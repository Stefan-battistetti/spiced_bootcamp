"""Twe following script is meant for being used for the TWITTER API-V2.
The least tweepy version to use is 4.01"""

import tweepy
import pytz
from credentials import *
import logging
import pymongo
import datetime
import time
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pycoingecko import CoinGeckoAPI


cg = CoinGeckoAPI()

### FUNCTION REGEX ###
mentions_regex = '@[A-Za-z0-9]+'
url_regex = 'https?:\/\/\S+'  # this will not catch all possible URLs
hashtag_regex = '#'
rt_regex = 'RT\s'


def clean_tweets(tweet):
    tweet = re.sub(mentions_regex, '', tweet)  # removes @mentions
    tweet = re.sub(hashtag_regex, '', tweet)  # removes hashtag symbol
    tweet = re.sub(rt_regex, '', tweet)  # removes RT to announce retweet
    tweet = re.sub(url_regex, '', tweet)  # removes most URLs

    return tweet


s = SentimentIntensityAnalyzer()


# create a connection to the mongodb running in the mongo container of the pipeline
mongo_client = pymongo.MongoClient("mongodb")
# create a new database called twitter
db = mongo_client.twitter


##### AUTHENTICATION #####
twitter_client = tweepy.Client(bearer_token=BEARER_TOKEN, consumer_key=API_KEY, consumer_secret=API_KEY_SECRET,
                               access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)


if twitter_client:
    logging.critical("\nAutentication OK")
else:
    logging.critical('\nVerify your credentials')

#### SEARCHING FOR TWEETS ####

# Defining a query search string
query = 'bitcoin OR btc OR cryptocurrency OR blockchain OR crypto OR money OR news OR currency OR coinbase OR trading OR bitcoincash OR usd OR gold lang:en -is:retweet'

end_time = datetime.datetime.now(
    pytz.timezone('Europe/Berlin')).timestamp()-259200
start_time = datetime.datetime.now(pytz.timezone(
    'Europe/Berlin')).timestamp()-(259200 + 7200)
print(end_time)
print(start_time)
h = 0
score = 0

# while datetime.datetime.now().timestamp() > end_time:
for i in range(252000, 0, -7200):
    logging.critical(
        f'\n\n\nINCOMING range:\n{i}\n{datetime.datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%dT%H:%M:%SZ")}\n\n')

    price_data = cg.get_coin_market_chart_range_by_id(
        'bitcoin', 'eur', start_time, end_time)
    trend_crypto = (
        ((price_data['prices'][-1][1])/(price_data['prices'][0][1]))-1)

    search_tweets = twitter_client.search_recent_tweets(
        query=query, tweet_fields=['id', 'text'], max_results=100, start_time=datetime.datetime.utcfromtimestamp(start_time).strftime("%Y-%m-%dT%H:%M:%SZ"), end_time=datetime.datetime.utcfromtimestamp(end_time).strftime("%Y-%m-%dT%H:%M:%SZ")
    )

    # print(search_tweets)

    for tweet in search_tweets.data:
        # logging.critical(f'\n\n\nINCOMING TWEET:\n{tweet.text}\n\n\n')
        aaa = (clean_tweets(str(tweet['text'])))
        # assuming your JSON docs have a text field
        sentiment = s.polarity_scores(aaa)
        # print(sentiment)
        #logging.critical(f'\n\n\nINCOMING TWEET:\n{aaa}\n\n\n')
        #print('I am working')
        # replace placeholder from the ETL chapter
        score += float(sentiment['compound'])

    # calculate the mean of score
    score_two_h = score/100
    # print(score_two_h)
    # print(trend_crypto)
    hour_date = datetime.datetime.utcfromtimestamp(
        end_time).strftime("%Y-%m-%d %H:%M:%S")

    #logging.critical(f'\n\n\nINCOMING HOUR:\n{hour_date}\n\n\n')

    # create a json record and inserting it in the collections called tweets
    record = {'id': h, 'timedate': hour_date,
              'sentiment': score_two_h, 'trend': trend_crypto}

    #logging.critical(f'\n\n\nINCOMING HOUR:\n{record}\n\n\n')

    # and inserting it in the collections called tweets
    # collection_name = 'tweets_0' + str(h)
    # print(collection_name)
    # db.collection_name.insert_one(record)
    db.tweets.insert_one(record)

    end_time = datetime.datetime.now(
        pytz.timezone('Europe/Berlin')).timestamp()-i
    start_time = datetime.datetime.now(
        pytz.timezone('Europe/Berlin')).timestamp()-(i+7200)

    score = 0

    h += 1

    # time.sleep(5)
