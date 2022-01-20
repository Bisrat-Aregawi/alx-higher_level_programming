#!/usr/bin/python3
"""Module makes POST request using `requests` module."""

if __name__ == "__main__":
    import requests
    from sys import argv

    payload = {'email': argv[2]}
    res = requests.post(argv[1], data=payload)
    print(res.text)
