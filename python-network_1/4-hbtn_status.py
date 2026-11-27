#!/usr/bin/python3
"""Fetch the intranet status page using requests."""
import requests

if __name__ == "__main__":
    urls = ["https://intranet.hbtn.io/status",
            "https://alu-intranet.hbtn.io/status"]
    for url in urls:
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException:
            continue
        print("Body response:")
        print("\t- type: {}".format(type(r.text)))
        print("\t- content: {}".format(r.text))
        break
