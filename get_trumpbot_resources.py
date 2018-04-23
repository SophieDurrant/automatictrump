from get_keys import *

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)

def _get_absolute_path(filename):
    return dir_path + "/" + filename

#note to self: encrypt
def get_keys():
    return {'consumer_key': consumer_key, 'consumer_secret': consumer_secret, 'access_token_key': access_token_key, 'access_token_secret': access_token_secret} 

def get_tweet_resource():
    return _get_absolute_path("tweets.txt")
    
def get_speech_resource():
    return _get_absolute_path("trump_speech.txt")

def get_tweet_json():
    return _get_absolute_path("tweet_model.json")

def get_speech_json():
    return _get_absolute_path("speech_model.json")
