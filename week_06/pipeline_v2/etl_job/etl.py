import logging
from credentials import *
from re import T
import pymongo
import pandas as pd
import time
from sqlalchemy import create_engine
import psycopg2
import matplotlib.pyplot as plt
import requests

# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client_slack = WebClient(token=token)
logger = logging.getLogger(__name__)


# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb")

# Select the database you want to use withing the MongoDB server
db = client.twitter

# docs = db.tweets.find(limit=5)
# for doc in docs:
#     logging.critical('\n', doc)

time.sleep(120)

pg = create_engine(
    'postgresql+psycopg2://postgres:postgres@postgresdb:5432/etl_db', echo=True)


# time.sleep(10)
# while True:
#     pass

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    id INT PRIMARY KEY,
    timedate VARCHAR(255),
    trend NUMERIC,
    sentiment NUMERIC
);
''')

docs = db.tweets.find()
for doc in docs:
    print(doc)
    id = doc['id']
    sentiment = doc['sentiment']
    trend = doc['trend']
    timedate = doc['timedate']
    print(timedate)
    query = "INSERT INTO tweets VALUES (%s, %s, %s, %s);"
    pg.execute(query, (id, timedate, trend, sentiment))
    # logging.critical(id, time_date, score, trend)

query5 = "SELECT * FROM tweets;"
tweets_and_trends = pd.read_sql(query5, pg)

tweets_and_trends['timedate'] = pd.to_datetime(
    tweets_and_trends['timedate'], format="%Y-%m-%d %H:%M:%S")
# tweets_and_trends.set_index('timedate', inplace=True)
# tweets_and_trends['hour'] = tweets_and_trends['timedate'].dt.hour
# tweets_and_trends["day"] = tweets_and_trends["timedate"].dt.day
# tweets_and_trends["day-hour"] = tweets_and_trends["hour"].dt.day

tweets_and_trends.to_csv('file.csv', index=False)
logging.critical(tweets_and_trends.head(20))
logging.critical(tweets_and_trends.info())


# plt.plot(data=tweets_and_trends, kind='line',
#          y='trend', x="timedate", color='blue')
# plt.plot(data=tweets_and_trends, kind='line',
#          y='sentiment', x='timedate', color='red')
plt.plot(tweets_and_trends.timedate,
         tweets_and_trends.trend*2, color='blue')
plt.xticks(rotation=45)
plt.plot(tweets_and_trends.timedate,
         tweets_and_trends.sentiment, color='red')
plt.xticks(rotation=45)
plt.legend(["Trend", "Sentiment"])
plt.savefig('tweets_and_trends.png', dpi=300,
            format='png', bbox_inches='tight')

text = 'Bitcoin Trends VS Tweets Sentiment CHART for the last 72 hours'

# data = {'text': text}

# The name of the file you're going to upload
file_name = "tweets_and_trends.png"
# ID of channel that you want to upload file to
channel_id = "C02U7QVJ3GB"

try:
    # Call the files.upload method using the WebClient
    # Uploading files requires the `files:write` scope
    result = client_slack.files_upload(
        channels=channel_id,
        initial_comment="Bitcoin Trends VS Tweets Sentiment CHART for the last 72 hours :smile:",
        file=file_name,
    )
    # Log the result
    logger.info(result)

except SlackApiError as e:
    logger.error("Error uploading file: {}".format(e))


# data = {{'text': text}, {"type": "image",
#                          "image_url": "tweets_and_trends.png", "alt_text": "bitcoin"}}
# data = {'text': text, "type": "image", "image_url": "https://i1.wp.com/thetempest.co/wp-content/uploads/2017/08/The-wise-words-of-Michael-Scott-Imgur-2.jpg?w=1024&ssl=1",
#         "alt_text": "Bitcoin Trends VS Tweets Sentiment"}

# data = {
#     "blocks": [
#         {
#             "type": "header",
#             "text": {
#                     "type": "plain_text",
#                     "text": text,
#             }
#         },
#         {
#             "type": "divider"
#         },
#         {
#             "attachments": [
#                 {
#                     "fallback": text,
#                     "image_url": "tweets_and_trends.png"
#                 }
#             ]
#         }
#     ]
# }


#             "type": "image",
#             "image_url": "https://i.imgur.com/BlgVqxUh.png",
#             "alt_text": "inspiration"
#         }
#     ]
# }


#requests.post(url=webhook_url, json=data)
