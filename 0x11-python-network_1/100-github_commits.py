#!/usr/bin/python3
'''evaluating candidates applying for backend
    position with multiple technical challenges'''

import requests
import sys

if __name__=="__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner,repo)

    r = requests.get(url)
    commits =r.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                     commits[i].get("sha"),
                     commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
