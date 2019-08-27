#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """

import requests

if __name__ == '__main__':
    url = 'https://intranet.hbtn.io/status'
    rta = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(rta.text)))
    print("\t- content: {}".format(rta.text))
