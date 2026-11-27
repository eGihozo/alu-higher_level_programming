#!/usr/bin/python3
"""Display the X-Request-Id header value of a URL using requests."""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get("X-Request-Id"))
