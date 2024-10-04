#!/usr/bin/python3
''' sends a post request to a url with letter as parameter'''

import requests
import sys

if __name__=="__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    data = {'q':letter}
    r = requests.post(url,data=data)

    try:
        body = r.json()

        if body == {}:
            print("No results")
        else:
            print("[{}] {}".format(body.get("id").body.get("name")))
    except ValueError:
         print("Not a valid JSON")
