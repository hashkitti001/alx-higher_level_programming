#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return None
    else:
        return max(a_dictionary)
