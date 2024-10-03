#!/bin/bash
# Sends a POST request with a JSON body from the file and displays the response body
curl -s -H "Content-Type: application/json" -d @"$2" "$1"

