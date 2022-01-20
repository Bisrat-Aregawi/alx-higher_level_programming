#!/usr/bin/python3
"""Module POSTs to an API to get JSON response.
POST to `http://0.0.0.0:5000/search_user` with data `q` and output a formated
text if user is found and a formated error text if JSON is not valid or is
empty.
"""


def search_user(url, data=''):
    """Function POSTs and handles errors.

    Args:
        url: URL to send POST request to
        data: Payload to append to @url

    Returns:
        None
    """
    payload = {'q': data}
    res = requests.post(url, data=payload)

    try:
        jsn = res.json()
        if jsn == {}:
            print("No result")
        else:
            print("[{}] {}".format(jsn.get('id'), jsn.get('name')))
    except Exception:
        print("Not a valid JSON")
    return None


if __name__ == "__main__":
    import requests
    from sys import argv

    try:
        search_user("http://0:5000/search_user", argv[1])
    except Exception:
        search_user("http://0:5000/search_user")
