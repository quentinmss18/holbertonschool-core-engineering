#!/usr/bin/env python3
"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """
    Defines a square by its size.
    """

    def __init__(self, size):
        """
        Initializes the square with a private size.

        Args:
            size: The side length of the square.
        """
        self.__size = size
