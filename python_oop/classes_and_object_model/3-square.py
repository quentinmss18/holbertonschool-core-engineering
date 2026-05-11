#!/usr/bin/env python3
"""
This module defines a Square class with an area method.
"""


class Square:
    """
    Defines a square, validates its size, and calculates its area.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The side length of the square (default 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculates the current square's area.

        Returns:
            The area of the square (size squared).
        """
        return self.__size ** 2
