#!/bin/bash
# Sends a GET request to the URL and displays the body of a 200 status code response
response=$(curl -s -w "%{http_code}" "$1" -o tmp.txt)
if [ "$response" -eq 200 ]; then
  cat tmp.txt
fi

