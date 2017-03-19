#!/usr/bin/env python3

 
import generatetrump
 
speech_model = generatetrump.SpeechModel()
tweet_model = generatetrump.TweetModel()
 
speech_model.regenerate()
tweet_model.regenerate()