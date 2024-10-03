#!/bin/bash
#Sends a post request to the passed url

curl -s -X POST -d "email=test@gmail.com" -d "Subject=I will always be here for PLD" "$1"
