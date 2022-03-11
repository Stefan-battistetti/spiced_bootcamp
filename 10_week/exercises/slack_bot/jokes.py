# curl -X POST -H 'Content-type: application/json' --data '{"text":"Hello, World!"}' 
#

#import pyjokes
import requests
import json
import sys
import random


webhook_url = "<URL>"

#joke = pyjokes.get_joke()

data = {    "blocks": [
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "Hey <!here|here>, it's time for <#C02R1678FT3>"
			}
		},
]
}

requests.post(url=webhook_url, json=data)


# if __name__ === ‘__main__’:
#      url = “<URL>”
#      message = (“A Sample message by bot”)
#      title = (f”New Incoming Message :zap:”)
#      slack_data = {
#     “username”: “AshBot”,
#     “icon_emoji”: “:satellite:”,
#     “channel” : “general”,
#     “attachments”: [
#     {
#       “color”: “#9737EE”,
#       “fields”: [
#       {
#        “title”: title,
#        “value”: message,
#        “short”: “false”,
#        }
#       ]}
#       ]}
#     byte_length = str(sys.getsizeof(slack_data))
#     headers = {‘Content-Type’: “application/json”, ‘Content-Length’:     byte_length}
#     response = requests.post(url, data=json.dumps(slack_data),    headers=headers)
#    if response.status_code != 200:
#        raise Exception(response.status_code, response.text)
