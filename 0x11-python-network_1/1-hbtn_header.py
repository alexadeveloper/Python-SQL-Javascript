#!/usr/bin/python3
""" displays the value of the X-Request-Id """

import urllib.request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        cabezera = dict(response.info())
        if 'X-Request-Id' in cabezera:
            print(cabezera['X-Request-Id'])
