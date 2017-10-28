#!/bin/bash
# usage:  addbulkfiles.sh file dbname
cat $1 | curl -H "Content-Type: application/json" -d @- -X POST $2/_bulk_docs
