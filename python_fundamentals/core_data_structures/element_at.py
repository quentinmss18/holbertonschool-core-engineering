#!/usr/bin/env python3

def element_at(my_list, idx):
    """
    Retrieves an element from a list at a specific index.
    Returns None if idx is negative or out of range.
    """
    # Check if idx is negative
    if idx < 0:
        return None

    # Check if idx is out of range (greater than or equal to list length)
    if idx >= len(my_list):
        return None

    return my_list[idx]
