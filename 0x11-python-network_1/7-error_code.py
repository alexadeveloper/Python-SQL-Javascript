#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    rta = requests.get(url)
    if rta.status_code != 200:
        print("Error code: {}".format(rta.status_code))
    else:
        print(rta.text)
