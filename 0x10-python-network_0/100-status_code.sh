#!/bin/bash
# displays the code of the response
curl $1 -sIw '%{http_code}' -o /dev/null
