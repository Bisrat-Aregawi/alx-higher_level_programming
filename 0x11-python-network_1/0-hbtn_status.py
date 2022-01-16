#!/usr/bin/python3
"""Module uses urllib to fetch content."""
import urllib.request

req = urllib.request.Request("https://intranet.hbtn.io/status")

with urllib.request.urlopen(req) as res:
    html = res.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf8')))
