#!/usr/bin/python3

# todo:
#    sort into functions
#    --add merge function
#

import json
import os
import subprocess
import pyexifinfo as exif
import sys

from pprint import pprint 

def importFile():
    with open('example.json') as data_file:
        data = json.load(data_file)
    return data

def exportFile():
    # write json to file.
    with open('output.json', 'w') as outfile:  
            stritem = json.dumps(jout, indent=4)
            outfile.write(stritem)

def walkfiles(argv):
    data = []
    for root, dirs, files in os.walk(argv):
        for name in files:
                p = os.path.join(root, name)
                datat = exif.get_json(p)
                datat[0]['hash'] = subprocess.check_output(['ipfs','add','-n', p]).split()[1].decode("utf-8")
                print(datat[0]['hash'])
                data.append(datat[0])
    return data


jout = walkfiles(sys.argv[1])
exportFile()




# broken/random code:
                #datat[0]['hash'] = subprocess.Popen(["ipfs", "add", "-n", p], stdout=subprocess.PIPE)
                #datat[0]['hash'] = subprocess.Popen(["echo", p], stdout=subprocess.PIPE)
#            p = subprocess.Popen(["exiftool", "-json", os.path.join(root, name)], stdout=subprocess.PIPE, shell=True)
#            (poutput, error) = p.communicate()
#            print(poutput)
# list
#p = '/home/potatoe/Musique/electro/64revolt/Aim_for_the_flat_top/64revolt_-_Alice_Sweet_Alice.mp3'
#print(datat[0]['File:FileSize'])
#p = subprocess.Popen(["exiftool", "-json", "/home/potatoe/Musique/electro/64revolt/Aim_for_the_flat_top/64revolt_-_Alice_Sweet_Alice.mp3"], stdout=subprocess.PIPE)
#(poutput, error) = p.communicate()
#print(poutput)

#pprint(json.load(onetime))


#data[0]['hash'] = 404040
#print(data[0]["SourceFile"]) 
#for item in jout:
#    pprint(item)
#for i,v in enumerate(data[0]):
#  print (i,v)

#for k in sorted(data[0]):
#    print (k, data[0][k])

#for k in data[0]:
#    print (k, ": ", data[0][k])

#jout = importFile()
#stritem = json.dumps(jout[0], ensure_ascii=False)


# "/home/potatoe/Musique/electro/64revolt"
