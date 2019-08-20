#!/bin/bash
# sends a request to that URL
curl -w '%{size_download}\n' -so /dev/null $1
