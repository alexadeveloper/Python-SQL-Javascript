#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests
from sys import argv

if __name__ == '__main__':
    palabra = argv[1]
    url = 'https://swapi.co/api/people/'
    rta = requests.get(url, params={'search': palabra})
    jdict = rta.json()
    print("Number of results: {}".format(jdict['count']))
    if jdict['count'] > 0:
        for i in jdict['results']:
            print(i['name'])
