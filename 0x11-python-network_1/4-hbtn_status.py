#!/usr/bin/python3
"""Module fetches from `https://intranet.hbtn.io/status.`."""

if __name__ == "__main__":
    import requests

    response = requests.get("https://intranet.hbtn.io/status")

    print("Body response:\n\t- type: {}\n\t- content: {}".
          format(type(response.text), response.text))
