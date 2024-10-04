#!/usr/bin/python3
''' takes in a url and sends a request
    to the url and displays the body of the resonse'''

import requests
import sys

if __name__=="__main__":
    url = sys.argv[1]

    request = requests.get(url)

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)

