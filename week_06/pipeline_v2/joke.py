# pip install pyjokes
import pyjokes
import requests

webhook_url = "https://hooks.slack.com/services/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"

joke = pyjokes.get_joke()

data = {'text': joke}
requests.post(url=webhook_url, json = data)
