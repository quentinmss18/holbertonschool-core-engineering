#!/usr/bin/env python3
"""
This module defines a Square class with property getters and setters.
"""


class Square:
    """
    Defines a square with private size, validation, and area calculation.
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
        """
        Getter for the private __size attribute.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the private __size attribute with validation.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the current square's area.

        Returns:
            The area of the square.
        """
        return self.__size ** 2
