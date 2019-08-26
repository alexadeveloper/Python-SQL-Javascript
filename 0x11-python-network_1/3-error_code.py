#!/usr/bin/python3
""" takes in a URL and an email, sends a POST and display the response """

import urllib.request
from sys import argv
import urllib.error

if __name__ == '__main__':
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            utf8 = response.read().decode('utf-8')
        print(utf8)
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
