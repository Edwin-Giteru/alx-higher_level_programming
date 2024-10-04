#!/usr/bin/python3
# takes a url and send a request url and displays the value
from urllib import request
import sys

url = sys.argv[1]

with request.urlopen(url) as response:
    headers = response.headers
    x_request_id = headers.get('X-Request-Id')
    print(x_request_id)

