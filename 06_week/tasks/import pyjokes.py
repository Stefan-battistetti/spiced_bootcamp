import pyjokes
import requests

webhook_url = "https://hooks.slack.com/services/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"

joke = pyjokes.get_joke()

data = {'text': joke}
requests.post(url=webhook_url, json = data)