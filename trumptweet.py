#!/usr/bin/env python3

import faketrump
import twitter

from get_trumpbot_resources import get_keys #twitter api secrets
#returns following data as dict:
#consumer_key
#consumer_secret
#access_token_key
#access_token_secret

def login():
    keys = get_keys()
    api = twitter.Api(**keys)
    return api

def tweet():
    status = api.PostUpdate(faketrump.tweet_combined())
  
api = login()   

if (__name__ == '__main__'):   
    tweet()