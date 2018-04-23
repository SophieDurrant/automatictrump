#!/usr/bin/env python3

from time import sleep
import trumptweet
import random

random.seed()

while (True):
    sleep(random.randint(60, 3600))
    trumptweet.tweet()
    


