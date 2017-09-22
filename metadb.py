#!/usr/bin/python3

import json
from pprint import pprint 

with open('example.json') as data_file:
    data = json.load(data_file)

data[0]['hash'] = 404040
#print(data[0]["SourceFile"]) 
pprint(data)
