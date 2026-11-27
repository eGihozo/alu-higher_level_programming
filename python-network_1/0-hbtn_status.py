#!/usr/bin/python3
"""Fetch the intranet status page using urllib."""
import urllib.error
import urllib.request

if __name__ == "__main__":
    urls = ["https://intranet.hbtn.io/status",
            "https://alu-intranet.hbtn.io/status"]
    for url in urls:
        try:
            with urllib.request.urlopen(url) as response:
                body = response.read()
                print("Body response:")
                print("\t- type: {}".format(type(body)))
                print("\t- content: {}".format(body))
                print("\t- utf8 content: {}".format(body.decode("utf-8")))
            break
        except urllib.error.URLError:
            continue
