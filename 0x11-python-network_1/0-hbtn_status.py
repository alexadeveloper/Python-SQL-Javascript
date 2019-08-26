#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """


import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        rta = response.read()
        format_utf8= rta.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(rta)))
    print("\t- content: {}".format(rta))
    print("\t- utf8 content: {}".format(format_utf8))
