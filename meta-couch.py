#!/usr/bin/python3


# todo:
#

import json, os, sys
import subprocess
import couchdb

from pprint import pprint 

def usage():
    print("Usage: ", sys.argv[0], " []")

def importFile(inputFilename):
    with open(inputFilename) as data_file:
        data = json.load(data_file)
    return data

def exportFile():
    # write json to file.
    with open('output.json', 'w') as outfile:  
            stritem = json.dumps(jout, indent=4)
            outfile.write(stritem)


data = importFile('example.json')
pprint(data)

if len(sys.argv) == 2:
    couch = couchdb.Server(sys.argv[1])
else:
    couch = couchdb.Server()

db = couch['metadb']
for item in data:
    db.save(item)

