import pandas as pd
import pyjokes
import requests
from faker import Faker


from sqlalchemy import create_engine
sqlengine = create_engine('postgresql://postgres:titanic99@postgresdb:5432/twitter', echo=True)



query = f'''
    SELECT * FROM tweets;
'''

df_tweet = pd.read_sql(query, sqlengine)




webhook_url ='https://hooks.slack.com/services/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'


for index,row in df_tweet.iterrows():
  
    
    text=str(row.iloc[0])
    sentiment= str(row.iloc[1])


    
    data={
        "blocks": [
            {
                "type": "divider"
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
            }
        ]
    }
  
    requests.post(url=webhook_url, json=data)




