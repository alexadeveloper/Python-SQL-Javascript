#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    rta = requests.get(url)
    cabezera = rta.headers
    if 'X-Request-Id' in cabezera:
        print(cabezera['X-Request-Id'])
