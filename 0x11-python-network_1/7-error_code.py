#!/usr/bin/python3
"""Module fetches and handles http error.

Takes a URL, sends a request using `requests` module and displays the body of
the response. If status code is above 400 inclusive, it will print an error
message.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    res = requests.get(argv[1])

    if res.status_code < 400:
        print(res.text)
    else:
        print("Error code: {}".format(res.status_code))
