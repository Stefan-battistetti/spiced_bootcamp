import pymongo
import time
import logging  # the luxury version of print
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

# Select the database you want to use withing the MongoDB server
db = client.twitter



#time.sleep(10)  

sqlengine = create_engine('postgresql://postgres:titanic99@postgresdb:5432/twitter', echo=True)

sqlengine.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    text text,
    sentiment NUMERIC
);
''')

analyser = SentimentIntensityAnalyzer()


docs = db.tweets.find({})
for doc in docs:
    print(doc)
    text = doc['text']
    #score = 1.0  # placeholder value
    score =analyser.polarity_scores(text)['compound']
    query = "INSERT INTO tweets VALUES (%s, %s);"
    sqlengine.execute(query, (text, score))




