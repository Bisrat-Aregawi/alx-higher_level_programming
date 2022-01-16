#!/usr/bin/python3
"""Module prints header value.

Module is responsible for taking URL passed as command line argument and
request content from server. It then prints the response header's
`X-Request-Id` value to the standard output
"""

if __name__ == "__main__":
    from sys import argv
    import urllib.request

    req = urllib.request.Request(argv[1])

    with urllib.request.urlopen(req) as res:
        print(res.headers.get("X-Request-Id"))
