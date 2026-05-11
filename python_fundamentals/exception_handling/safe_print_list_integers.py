#!/usr/bin/env python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers.

    Args:
        my_list: The list containing elements of any type.
        x: The number of elements to access from my_list.

    Returns:
        The number of integers actually printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
