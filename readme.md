
# 'universal' media metadata database

The idea is to create a distributed database of file metadata.  Identifiable by ipfs hashes, so that if the media exists on ipfs it can be retrieved. 

There could be a script which anyone could run on a directory of media files, which would produce a JSON file with hashes and metadata for each file using some meta-data extraction tool, which might differ depending on file format.  This is then added to other versions of the database from peers.

## Computing hashes
The simplest way to do this would be with: 

    IPFS add -n <file>

Which produces the hash without actually adding any data to ipfs.
This would require ipfs to be installed.  Another way would be using 'Multihash' tool which IPFS uses.

## Extracting metadata

There are many tools available, the most universal that comes to mind is 'exiftool' 
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
