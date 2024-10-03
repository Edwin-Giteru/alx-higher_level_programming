#!/bin/bash
# Makes a request to the specified URL to receive the response containing 'You got me!'
curl -s -X PUT -d "user_id=98" -H "Origin: School" 0.0.0.0:5000/catch_me

