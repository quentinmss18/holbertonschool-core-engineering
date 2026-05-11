#!/usr/bin/env python3
def safe_print_division(a, b):
    """
    Divides two integers and prints the result using finally.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of the division, or None if an error occurred.
    """
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(result))
    return result
