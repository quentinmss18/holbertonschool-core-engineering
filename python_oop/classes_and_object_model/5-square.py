#!/usr/bin/env python3
"""
This module defines a Square class that can print itself.
"""


class Square:
    """
    Defines a square with printing capabilities.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): The side length of the square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the # character to stdout.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
