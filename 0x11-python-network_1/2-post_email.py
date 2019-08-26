#!/usr/bin/python3
""" takes in a URL and an email, sends a POST and display the response """

import urllib.request
from sys import argv

if __name__ == '__main__':
    url = argv[1]
    email = argv[2]
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')
    respuesta = urllib.request.Request(url, data)
    with urllib.request.urlopen(respuesta) as response:
        utf8 = response.read().decode('utf-8')
    print(utf8)
