#!/usr/bin/python3
''' takes in a url and an email address
    ,sends a post request to a the passed
    url with email as a parameter'''
    
import requests
import sys

if __name__=="__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email':email}
    r = requests.post(url,data =data)
    content = r.json()
    print(content.get("email"))
