#!/usr/bin/python3
# script that takes url and sends a request to the url and displays the body of the response
#!/usr/bin/python3
# Sends a request to a URL and displays the body of the response (handles HTTP errors)

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode("utf-8")
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


