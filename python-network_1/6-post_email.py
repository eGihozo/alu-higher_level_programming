#!/usr/bin/python3
"""POST an email to a URL using requests and display the body."""
import requests
import sys

if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(r.text)
