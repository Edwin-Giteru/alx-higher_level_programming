#!/usr/bin/python3
''' takes my github credentials and
    uses githu API to display your id '''

import requests
import sys
from requests.auth import HTTPBasicAuth

if __name__=="__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username,password)
    r = requests.get(url,auth=auth)

    if r.status_code == 200:
        try:
            body = r.json()
            if not body:
                print("None")
            else:
                print(body.get("id"))

        except ValueError:
            print("Invalid json file")
    else:
        print("None")


