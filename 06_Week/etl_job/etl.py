
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pymongo
from sqlalchemy import create_engine

time.sleep(30)

s  = SentimentIntensityAnalyzer()

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use withing the MongoDB server
db = client.twitter

docs = db.twitter.find()

pg = create_engine('postgresql://postgres:loop@postgresdb:5432/postgres', echo=True)

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text TEXT,
    sentiment NUMERIC,
    id SERIAL
);
''')
while True:
    for doc in docs:
        sentiment = s.polarity_scores(doc['text'])  # assuming your JSON docs have a text field
        print(sentiment)
        text = doc['text']
        score = sentiment['compound']
        query = "INSERT INTO tweets VALUES (%s, %s);"
        pg.execute(query, (text, score))
        time.sleep(10)