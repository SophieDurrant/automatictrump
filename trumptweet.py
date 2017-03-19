#!/usr/bin/env python3

import faketrump
import twitter
from time import sleep

from getkeys import get_keys #twitter api secrets
#returns following data as dict:
#consumer_key
#consumer_secret
#access_token_key
#access_token_secret



def login():
    keys = get_keys()
    api = twitter.Api(**keys)
    return api

api = login()

def tweet():
    status = api.PostUpdate(faketrump.tweet_combined())
        
tweet()
