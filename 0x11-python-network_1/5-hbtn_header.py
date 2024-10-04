#!/usr/bin/python3
''' a script that takes a url sends a request
    to the url and diplays the value of the variable X-Request-Id'''

import requests
import sys

if __name__=="__main__":
    url = sys.argv[1]

    r = requests.get(url)
    d = r.headers.get('X-Request-Id')
    print(d)
