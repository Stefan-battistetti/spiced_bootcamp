
#print('hello world')

import pymongo
import time
from sqlalchemy import create_engine
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


time.sleep(5)

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use withing the MongoDB server
db = client.twitter


#df = pd.DataFrame(search_tweets, columns=['tweet_text'])
#df = pd.DataFrame(docs)
#df.to_sql('tweets', pg, if_exists='replace')
# docs = db.collections.tweets.find()
# for doc in docs:
#     print('###############PRINTSTATEMENT#######################', doc)

s  = SentimentIntensityAnalyzer()

pg = create_engine('postgresql://postgres:titanic99@postgresdb:5432/twitter', isolation_level="AUTOCOMMIT", echo=True)


pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment text
);
''')

entries = db.collections.tweets.find()

while True:
    for entry in entries:
        text = entry['text']
        sentiment = s.polarity_scores(entry['text'])  # assuming your JSON docs have a text field
        print(sentiment)
        score = sentiment['compound']
        query = "INSERT INTO tweets VALUES (%s, %s);"
        pg.execute(query, (text, score))
        time.sleep(2)