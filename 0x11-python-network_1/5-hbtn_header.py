#!/usr/bin/python3
"""Module fetches using `requests` module.
Show `X-Request-Id` header's value.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get(argv[1])

    print("{}".format(res.headers.get('X-Request-Id')))
