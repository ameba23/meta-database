#!/usr/bin/python3


# todo:
#    allow user to define output file or stdout
#    --add merge function
#

import json, os, sys
import subprocess
import getopt
import pyexifinfo as exif

from pprint import pprint 

def usage():
    print("Usage: ", sys.argv[0], "[options] [path(s) or file(s)]")
    print(" -a, --addfiles    add files to IPFS rather than just extracting metadata")
    print(" -h, --help        display this message")
    print(" -v, --version     display version information and exit")

def importFile():
    with open('example.json') as data_file:
        data = json.load(data_file)
    return data

def exportFile(bulkfiles, outfilename):
    # write json to file.
    with open(outfilename, 'w') as outfile:  
            stritem = json.dumps(bulkfiles, indent=4)
            outfile.write(stritem)

def getMetadata(p, data):
    print("Extracting metadata from ", p)
    datat = exif.get_json(p)
    if addfiles:
        commandstr = ['ipfs','add', p]
    else:
        commandstr = ['ipfs','add','-n', p]
    datat[0]['_id'] = subprocess.check_output(commandstr).split()[1].decode("utf-8")
    print(datat[0]['_id'])
    data.append(datat[0])
    return data

def walkfiles(argv):
    data = []
    if os.path.isdir(argv):
        for root, dirs, files in os.walk(argv):
            for name in files:
                data = getMetadata(os.path.join(root, name), data)
    else:
        data = getMetadata(argv, data)
    return data


try:
    options, args = getopt.getopt(sys.argv[1:], 'avho', ['addfiles','version','help', 'output'])
except getopt.GetoptError as err:
    print(err)
    usage()
    sys.exit(2)

print(options) 
print(args)

outputfile = ""
addfiles = False
for o, a in options:
    if o in ("-a", "--addfiles"):
        addfiles = True
        print("adding files")
    if o in ("-h", "--help"):
        usage()
        sys.exit()
    if o in ("-v", "--version"):
        print("version 0")
        sys.exit()
    if o in ("-o", "--output"):
        outputfile = a
if args == []:
    usage()
    sys.exit()


jout = []
for patharg in args:
    if os.path.exists(patharg):
        jout.append(walkfiles(patharg))
    else:
        usage()
        print("Path or file does not exist")
        sys.exit(2)


# if something was found
if len(jout) > 0:
    # wrap into a single element called docs (required by couchdb bulk docs)
    bulkfiles = {"docs":jout}
    if outputfile != "":
        exportFile(bulkfiles, outputfile)
    else:
        #write to std out
        pprint(bulkfiles)

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
