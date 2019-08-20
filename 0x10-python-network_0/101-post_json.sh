#!/bin/bash
# displays the code of the response
curl $1 -sX POST -H "Content-Type: application/json" -d @$2
