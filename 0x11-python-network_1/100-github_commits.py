#!/usr/bin/python3
"""Module pulls 10 latest commits of a repo to a specific user.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get('https://api.github.com/repos/{}/{}/commits'.
                     format(argv[2], argv[1]))

    count = 0
    for elem in r.json():
        if count < 10:
            print("{}: {}".format(elem.get('sha'), elem.
                                  get('commit').
                                  get('author').
                                  get('name')))
        count += 1
