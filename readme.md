
# 'Universal' media metadata database

The idea is to create a distributed database of file metadata, identifiable by [IPFS](https://github.com/ipfs/ipfs) hashes, so that if the media exists on ipfs it can be retrieved. 

There could be a script which anybody could run on a directory of media files, which would produce a JSON file with hashes and metadata for each file using some meta-data extraction tool, which might differ depending on file format.  This is then collated with other versions of the database from peers.

## Beginnings of a web frontend to the couchdb in Ruby with Sinatra

This is hosted in a separate repository [ameba23/meta-sinatra](https://github.com/ameba23/meta-sinatra)

## Computing hashes
The simplest way to do this would be with: 

    ipfs add -n <file>

Which produces the hash without actually adding any data to ipfs.
Quick and dirty way to tidy output from this command:

    ipfs add -n <file> | cut -d ' ' -f 2

This would require ipfs to be installed.  Another way would be by using [multihash](https://github.com/multiformats/multihash), the future-proof hashing tool which IPFS uses.  However since IPFS divides bigger files into blocks, at the moment using 'ipfs add' itself seems to be the most reliable way to ensure the hash of the file will be the same as it is created on IPFS. 

## Extracting metadata

There are many tools available for specific filetypes, the most universal that comes to mind is Phil Harvey's [exiftool](https://sno.phy.queensu.ca/~phil/exiftool/). Although it specialises in image metadata, it is a robust tool for a wide variety of formats, which can generate JSON output, and can also be used in a variety of programming languages. 

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

Even for a file whose format is unknown or unreadable to exiftool, it gives us basic metadata from the filesystem which is useful to this project such as filename and size.

We would like metadata from as wide a range of formats as possible, and to cover:
* Images
* Audio
* Video
* Documents and ebooks
* Software?  Achives?

Another approach would be to using existing data from databases the user already has installed for example, [Music Player Daemon](https://www.musicpd.org/) or Calibre (ebook cataloging software).  A simple script could dump an MPD database to JSON.  

### todo
- handle directories.  try to be clever about when to include metadata for say an album, or a film with extra files such as subtitles bundled together.
- exiftool doesnt recognise .m3u files -use some other tool
- library genesis indexes books by md5, so it would be useful to add md5 hash as metadata for books, as then we can link to metadata from libgen.
- find and add musicbrainz id for audio files?
- cddb?

## Database system

[Apache CouchDB](https://couchdb.apache.org/) has some interesting features which make it a good candidate for this project.  Since there will be a variety of file formats, the metadata available is likely to vary greatly, making a relational database inappropriate,  and CouchDB is document driven.  Also CouchDB stores modified data as 'revisions' making it possible for the database to be modified by multiple peers even if they are not always connected to each other. 

## Merging and resolving conflicting data

All metadata associated with a hash is put together.  Ways of resolving incorrect or conflicting data could be devised, possibly by making the assumption that the majority of copies of the file have genuine metadata.

Links could be made between different version of the same media using a tagging system.  For example the same media in a different format or language. 
This tagging system could also be used to create links to established databases such as Discogs, IMdb, Library Genesis. 

Bittorrent magnet links could also be added as metadata. 

To keep the database smaller, embedded images such as album artwork would not be included directly but referenced by a hash. 

## Uses

The nature of IPFS is that files are addressed by hashes.  There are already some efforts to index and search files on IPFS, which is not an easy task.  The idea of this project is to have a searchable, distributed media database which gives IPFS hashes even if the file is not available on IPFS **yet**.  

The database could be queried by using a web interface or command line tool.  

## python3 script to extract metadata to JSON

Usage:
```
Usage:  python metadb.py [options] [path(s) or file(s) to extract metadata from]
 -o file, --output=file   write to file rather than stdout
 -a, --addfiles           add files to IPFS rather than just extracting metadata
 -h, --help               display this message
 -v, --version            display version information and exit
```

Requires:
* IPFS
* [pyexifinfo](https://github.com/guinslym/pyexifinfo)

## bash script to add JSON file to couchdb database 

```
usage:  addbulkfiles.sh file http://user:pw@host/metadb
```

This is a one line script to use curl to add dump the file into couchdb using '_bulk_docs'.

This could be added to the first script to extract data and add it to the database in one swoop.  This was not done by default because it allows users to run the extraction to a file without needing to have access to the db.  The web front-end will also have a way of importing files to the db.

This will create (if it does not already exist) a database called 'metadb'.
(todo: check this works with bulkdocs if no db exists)



## Similar or related projects

To not re-invent the wheel, it would be good to know about similar projects which already exist. 
* [DML - Distributed magnet links](https://github.com/rakoo/dml)
* [metabin - Advanced file sharing platform](https://github.com/metabin/metabin#problems)
* [ipfs-search](https://github.com/ipfs-search/ipfs-search)
* [magnetico](https://github.com/boramalper/magnetico)
* [antilibrary](https://github.com/antilibrary)
* orbitdb?  pubsub? other attempts at ipfs indexing
