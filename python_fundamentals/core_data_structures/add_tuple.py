#!/usr/bin/env python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples.
    Returns a tuple of 2 integers:
    - The first element is the sum of the first elements of each tuple.
    - The second element is the sum of the second elements of each tuple.
    """
    # Extract the first two elements of tuple_a or use 0 if they don't exist
    a1 = tuple_a[0] if len(tuple_a) >= 1 else 0
    a2 = tuple_a[1] if len(tuple_a) >= 2 else 0

    # Extract the first two elements of tuple_b or use 0 if they don't exist
    b1 = tuple_b[0] if len(tuple_b) >= 1 else 0
    b2 = tuple_b[1] if len(tuple_b) >= 2 else 0

    return (a1 + b1, a2 + b2)
