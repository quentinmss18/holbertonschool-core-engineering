#!/usr/bin/env python3

def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value.
    If the dictionary is None or empty, returns None.
    """
    if not a_dictionary:
        return None

    # Using max() with the dictionary's get method as the comparison key
    return max(a_dictionary, key=a_dictionary.get)
