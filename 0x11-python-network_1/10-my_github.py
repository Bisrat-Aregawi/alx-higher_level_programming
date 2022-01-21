#!/usr/bin/python3
"""Module prints id of authenticated user on GitHub.

Uses `requests` module's HTTPBasicAuth method to fetch user's metadata and
display the id of the user. If credentials are not correct, it prints out
`None` to stdout.
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    from requests.auth import HTTPBasicAuth

    r = requests.get('https://api.github.com/user',
                     auth=HTTPBasicAuth(argv[1], argv[2]))

    print(r.json().get('id') or "None")
