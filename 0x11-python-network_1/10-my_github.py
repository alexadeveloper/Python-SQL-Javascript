#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests
from sys import argv

if __name__ == '__main__':
    usuario = argv[1]
    contrase = argv[2]
    rta = requests.get('https://api.github.com/user', auth=(usuario, contrase))
    if rta.status_code != 200:
        print('None')
    else:
        jdict = rta.json()
        print(jdict['id'])
