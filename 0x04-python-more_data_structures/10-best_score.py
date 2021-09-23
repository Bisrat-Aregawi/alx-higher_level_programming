#!/usr/bin/python3
def best_score(a_dictionary):
    best_key, value = "", 0
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > value:
                best_key, value = k, v
        return best_key
    return None
