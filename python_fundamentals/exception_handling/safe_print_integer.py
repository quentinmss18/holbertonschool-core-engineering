#!/usr/bin/env python3
def safe_print_integer(value):
    """
    Prints an integer using "{:d}".format().

    Args:
        value: The value to print (can be any type).

    Returns:
        True if value was successfully printed as an integer, False otherwise.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
