#!/bin/bash
# all HTTP methods
curl -sI $1 | grep Allow | cut -b 8-
