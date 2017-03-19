#!/usr/bin/env python3

import random
import generatetrump
import markovify


speech_model = generatetrump.SpeechModel()
tweet_model = generatetrump.TweetModel()

combined_model = markovify.combine([speech_model.model, tweet_model.model], [0.25,1])


overlap = {'max_overlap_ratio': 0.8, 'max_overlap_total': 20}


random.seed()

def generate_speech(size= 50):
    speech = ""
    for i in range(size):
        sentence = speech_model.model.make_sentence(**overlap)
        speech = speech + sentence + random.choice([" ", "\n\n"])
    return speech

def write_speech(filename):
    generate_speech()
    with open(filename, "w") as f:
        f.write(speech)

def print_speech():
        print(generate_speech())
        
def tweet(model):
    tweet = ""
    for i in range(7):
        sentence = model.make_short_sentence(140, **overlap)
        sentence = sentence.replace("&amp;", "&")
        new_tweet = tweet + sentence + " " 
        if len(new_tweet) <= 141:
            tweet = new_tweet
            
    tweet = tweet[:-1]
    return tweet

def tweet_standard():
    return tweet(tweet_model.model)

def tweet_combined():
    return tweet(combined_model)

#TODO handle all the errors when Trump doesn't have an opinion on an issue.
def print_issue(issue):
    print(tweet_model.model.make_sentence_with_start(issue, **overlap))


