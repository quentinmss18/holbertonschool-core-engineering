#!/usr/bin/env python3
"""
This module defines a Square class with size validation.
"""


class Square:
    """
    Defines a square and validates its size.
    """

    def __init__(self, size=0):
        """
        Initializes the square with validation.

        Args:
            size (int): The side length of the square (default 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
