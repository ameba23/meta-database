
# 'universal' media metadata database

The idea is to create a distributed database of file metadata.  Identifiable by ipfs hashes, so that if the media exists on ipfs it can be retrieved. 

There could be a script which anyone could run on a directory of media files, which would produce a JSON file with hashes and metadata for each file using some meta-data extraction tool, which might differ depending on file format.  This is then added to other versions of the database from peers.

## Computing hashes
The simplest way to do this would be with: 

    IPFS add -n <file>

Which produces the hash without actually adding any data to ipfs.
This would require ipfs to be installed.  Another way would be using 'Multihash' tool which IPFS uses.

## Extracting metadata

There are many tools available, the most universal that comes to mind is Phil Harvey's [exiftool](https://sno.phy.queensu.ca/~phil/exiftool/). Although it specialises in image metadata, it is a robust tool for a wide variety of formats, which can generate JSON output.  
Here is an example of exiftool's output for an MP3 audio file with an ID3 Tag:

```
[{
  "SourceFile": "16. dj floorclearer - there's a wocket in my pocket.mp3",
  "ExifToolVersion": 10.55,
  "FileName": "16. dj floorclearer - there's a wocket in my pocket.mp3",
  "Directory": ".",
  "FileSize": "5.0 MB",
  "FileModifyDate": "2017:07:26 13:37:32+02:00",
  "FileAccessDate": "2017:09:21 13:03:51+02:00",
  "FileInodeChangeDate": "2017:07:26 13:37:32+02:00",
  "FilePermissions": "rw-r--r--",
  "FileType": "MP3",
  "FileTypeExtension": "mp3",
  "MIMEType": "audio/mpeg",
  "MPEGAudioVersion": 1,
  "AudioLayer": 3,
  "AudioBitrate": "224 kbps",
  "SampleRate": 44100,
  "ChannelMode": "Stereo",
  "MSStereo": "Off",
  "IntensityStereo": "Off",
  "CopyrightFlag": false,
  "OriginalMedia": false,
  "Emphasis": "None",
  "Encoder": "LAME3.92 ",
  "LameVBRQuality": 4,
  "LameQuality": 5,
  "LameMethod": "CBR",
  "LameLowPassFilter": "19.4 kHz",
  "LameBitrate": "224 kbps",
  "LameStereoMode": "Stereo",
  "ID3Size": 2289,
  "Title": "There's A Wocket In My Pocket",
  "Artist": "DJ Floorclearer",
  "Album": "Now That's What I Call Wrong Music Volume 5!",
  "Year": "",
  "Comment": "",
  "Genre": "None",
  "Duration": "0:03:08 (approx)"
}]
```

We would like metadata from as wide a range of formats as possible, and to cover:
* Images
* Audio
* Video
* Documents and ebooks
* Software?  Achives?

Another approach would be to using existing data from, for example, MPD. 

## Merging and resolving conflicting data

All metadata associate with a hash is put together.  Ways of resolving incorrect or conflicting data could be devised, possibly by making the assumption that the majority of copies of the file are genuine.

Links could be made between different version of the same media using a tagging system.  For example the same media in a different format or language. 
This tagging system could also be used to create links to established databases such as Discogs, IMdb, Library Genesis. 

Bittorrent magnet links could also be added as metadata. 

To keep the database smaller, embedded images such as album artwork would not be included directly but referenced by a hash. 

## Uses

The database could be queried by using some web interface or command line tool.

## Similar projects

To not re-invent the wheel, it would be good to know about similar projects which already exist. 
