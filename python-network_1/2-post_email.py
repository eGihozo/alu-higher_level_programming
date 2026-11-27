#!/usr/bin/python3
"""POST an email to a URL using urllib and display the response body."""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("utf-8")
    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
