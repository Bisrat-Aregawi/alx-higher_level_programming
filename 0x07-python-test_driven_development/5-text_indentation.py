#!/usr/bin/python3
"""Defines text_indentation function."""


def text_indentation(text):
    """Write text with 2 new lines when conditions are met.

    Prints text content and when encountered either of the following
    characters, it prints two new lines after.

    Args:
        text (str): string of characters

    Returns:
        None

    Raises:
        TypeError: if @text is not a string type
    """
    chars = ['.', '?', ':']
    prev = ""
    if isinstance(text, str):
        for ch in enumerate(text):
            if ch[1] == '.' or ch[1] == '?' or ch[1] == ':':
                prev = ch[1]
                print(ch[1], end="")
                print("\n")
            else:
                if prev in chars:
                    if ch[1] == ' ':
                        continue
                    else:
                        prev = ""
                        print(ch[1], end="")
                        continue
                print(ch[1], end="")
    else:
        raise TypeError("text must be a string")

    return None
