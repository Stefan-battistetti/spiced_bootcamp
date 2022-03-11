
import time
import requests
import json
import sys
import random
import pandas as pd
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.dialects import postgresql

#pg = create_engine('postgresql://postgres:titanic99@0.0.0.0:5555/twitter', echo=True) #if the slack_bot is started manually from the host
pg = create_engine('postgresql://postgres:titanic99@postgresdb:5432/twitter', echo=True)


tweets_query = pg.execute('''
	SELECT * 
	FROM tweets
	;
''')


#Old webhook from slack app
#webhook_url = "https://hooks.slack.com/services/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"

webhook_url = "https://hooks.slack.com/services/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"


df_tweets = pd.DataFrame(tweets_query, columns=['text','sentiment'])

#print(df_tweets)

#U02UU4QAK50

for row in df_tweets.iterrows():
	text= str(row.iloc[0])
	sentiment=str(row.iloc[1])
	#print('Text', text)
	#print('sentiment',sentiment)
	#data = {'Text':text}
	data = {'Text':text,'Senitment':sentiment}
	data = {  
		  "blocks": [
				{
						"type":"divider"
				},
				{	
						"type": "section",
						"text": {
						"type": "plain_text",
						"text": text	
					}
				},
				{	
						"type": "section",
						"text": {
						"type": "plain_text",
						"text": sentiment	
					}
				},
	]
	}
	requests.post(url=webhook_url, json=data)
	time.sleep(3600)



# data = {    "blocks": [
# 		{
# 			"type": "section",
# 			"text": {
# 				"type": "mrkdwn",
# 				"text": "Hey <!here|here>, it's time for <#C02R1678FT3>"
# 			}
# 		},
# ]
# }

# requests.post(url=webhook_url, json=data)
