#!/usr/bin/python3
"""Module requests using GET and handles HTTPError exceptions"""

if __name__ == "__main__":
    import urllib.error
    from sys import argv
    import urllib.request

    req = urllib.request.Request(argv[1])

    try:
        with urllib.request.urlopen(req) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
