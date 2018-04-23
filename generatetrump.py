 #!/usr/bin/env python3
import markovify
from os.path import isfile
from get_trumpbot_resources import *

default_state_size = 2

text_model = markovify.Text

class Generator:
    def generate(self, resource):
        pass

class TweetGenerator(Generator):
    def generate(self, resource):
        trump_tweets = ""
        with open(resource) as f:
            for line in f:
                fields = line.split(",")
                if len(fields) >= 3:
                    trump_tweets = trump_tweets + fields[1] + "\n\n"
            
        return text_model(trump_tweets, state_size = default_state_size)

class LongTextGenerator(Generator):
    def generate(self, resource):
        with open(resource) as f:
            trump_speeches = f.read()
        
        return text_model(trump_speeches, state_size = default_state_size)
    

class Model:
    def write_to_json(self):
        with open(self.json_file, "w") as f:
            f.write(self.model.chain.to_json())

    def regenerate(self):
        self.model = self.generator_strategy.generate(self.generator_file)
        self.write_to_json()
        
    
    def __init__(self, json_file, generator_file, generator_strategy):
        self.json_file = json_file
        self.generator_file = generator_file
        self.generator_strategy = generator_strategy
        
        if isfile(json_file):
            with open(self.json_file) as f:
                self.model = text_model.from_chain(f.read())
        else:
            self.regenerate()

class SpeechModel(Model):
    def __init__(self):
        Model.__init__(self, get_speech_json(), get_speech_resource(),
                       LongTextGenerator())

class TweetModel(Model):
    def __init__(self):
        Model.__init__(self, get_tweet_json(),
                       get_tweet_resource(),
                       TweetGenerator())
