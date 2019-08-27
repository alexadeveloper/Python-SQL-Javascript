#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    rta = requests.get(url, data)
    print(rta.text)
