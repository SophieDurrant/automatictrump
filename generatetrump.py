 #!/usr/bin/env python3
import markovify
import requests
from os.path import isfile

class Generator:
    def generate(self, resource):
        pass

class TweetGenerator(Generator):
    def generate(self, resource):
        trump_tweets = ""
        r = requests.get(resource)
        for line in r.iter_lines():
            fields = line.decode(r.encoding).split(",")
            if len(fields) >= 3 and fields[1] == "Twitter for Android":
                trump_tweets = trump_tweets + fields[2] + "\n\n"
            
        return markovify.Text(trump_tweets, state_size = 3)

class LongTextGenerator(Generator):
    def generate(self, resource):
        with open(resource) as f:
            trump_speeches = f.read()
        
        return markovify.Text(trump_speeches, state_size = 3)
    

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
                self.model = markovify.Text.from_chain(f.read())
        else:
            self.regenerate()

class SpeechModel(Model):
    def __init__(self):
        Model.__init__(self, "speech_model.json", "~/trump.txt",
                       LongTextGenerator())

class TweetModel(Model):
    def __init__(self):
        Model.__init__(self, "tweet_model.json",
                       "https://raw.githubusercontent.com/bpb27/political_twitter_archive/master/realdonaldtrump/realdonaldtrump.csv",
                       TweetGenerator())
