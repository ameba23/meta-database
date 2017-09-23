#!/usr/bin/python3

import json
import os
import subprocess

from pprint import pprint 

#for root, dirs, files in os.walk("/home/potatoe/Musique/electro/64revolt"):
#    for name in files:
#            p = subprocess.Popen(["exiftool", "-json", os.path.join(root, name)], stdout=subprocess.PIPE, shell=True)
#            (poutput, error) = p.communicate()
#            print(poutput)

p = subprocess.Popen(["exiftool", "-json", "/home/potatoe/Musique/electro/64revolt/Aim_for_the_flat_top/64revolt_-_Alice_Sweet_Alice.mp3"], stdout=subprocess.PIPE)
(poutput, error) = p.communicate()
print(poutput)

#pprint(json.load(onetime))
with open('example.json') as data_file:
    data = json.load(data_file)

data[0]['hash'] = 404040
#print(data[0]["SourceFile"]) 
#pprint(data)
#for i,v in enumerate(data[0]):
#  print (i,v)

#for k in sorted(data[0]):
#    print (k, data[0][k])

#for k in data[0]:
#    print (k, ": ", data[0][k])

# then write json file.





#with open('output.json', 'w') as outfile:  
#    json.dump(data, outfile)
