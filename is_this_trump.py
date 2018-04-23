#!/usr/bin/env python3

import requests
import faketrump

def get_genuine_tweet():
    r = requests.get(resource)
    i = 0;
    for line in r.iter_lines():
        fields = line.decode(r.encoding).split(",")
        if len(fields) >= 3 and fields[1] == "Twitter for Android":
            