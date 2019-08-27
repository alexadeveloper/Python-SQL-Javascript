#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 1:
        rta = requests.post(url, data={'q': ""})
    if len(argv) > 1:
        rta = requests.post(url, data={'q': letter})
    try:
        jdict = rta.json()
        if jdict == {}:
            print("No result")
        else:
            print("[{}] {}".format(jdict['id'], jdict['name']))
    except valueError:
        print("Not a valid JSON")
