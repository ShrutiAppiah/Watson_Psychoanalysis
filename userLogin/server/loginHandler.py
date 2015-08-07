# See https://github.com/contextio/Python-ContextIO for a guide
# this will be changed to flask syntax

import requests
import contextio as c

# contextio key and secret key
CONSUMER_KEY = 'l57sr7jp'
CONSUMER_SECRET = 'm0mRv5iaojsNWnvu'

context_io = c.ContextIO(
    consumer_key=CONSUMER_KEY, 
    consumer_secret=CONSUMER_SECRET
)

requests.get
