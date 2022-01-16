#!/usr/bin/python3
"""Module requests using POST.

Module will take URL & email from cmdline argument and make a POST request.
Then it will display the UTF-8 decoded body of the response.
"""

if __name__ == "__main__":
    import urllib.parse
    from sys import argv
    import urllib.request

    url = argv[1]
    value = {"email": argv[2]}

    data = urllib.parse.urlencode(value).encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
