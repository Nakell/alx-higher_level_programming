#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    max_score = None
    if a_dictionary:
        for key, value in a_dictionary.items():
            if max_score is None or value > max_score:
                max_score = value
                best_key = key
    return best_key
