import tweepy
from credentials import *
import logging

client = tweepy.Client(bearer_token=BEARER_TOKEN,consumer_key=API_KEY,consumer_secret=API_KEY_SECRET,
access_token=ACCESS_TOKEN,access_token_secret=ACCESS_TOKEN_SECRET)

if client:
    logging.critical("\nAutentication OK")
else:
    logging.critical('\nVerify your credentials')


elon = client.get_user(username='elonmusk',user_fields=['name','id','created_at'])
#print(elon)

print(f'the user with name {elon.data.name} and ID {elon.data.id} created its twitter account on {elon.data.created_at}')


elon_tweets = client.get_users_tweets(id=elon.data.id, tweet_fields=['id','text','created_at'],max_results=5)
print(elon_tweets.data)
for tweet in elon_tweets.data:
    print(f"the user {elon.data.name} at {tweet.created_at} wrote:{tweet.text}\n")

query = 'climate change lang:en -is:retweet'  


search_tweets = client.search_recent_tweets(query=query,tweet_fields=['id','created_at','text'], max_results=10)
#print(search_tweets)
for tweet in search_tweets.data:
    logging.critical(f'\n\n\nINCOMING TWEET:\n{tweet.text}\n\n\n')

paginator = tweepy.Paginator(client.search_recent_tweets,tweet_fields=['id','created_at','text'], query=query).flatten(limit=10)
print(paginator)
for tweet in paginator:
    logging.critical(f'\n\n\nINCOMING TWEET ID {tweet.id}:\n{tweet.text}\n\n\n')
    file = open('fetched_tweets.txt',mode='a')
    file.write(tweet.text)
    file.close()
