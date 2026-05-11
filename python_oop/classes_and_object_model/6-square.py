#!/usr/bin/env python3
"""
This module defines a Square class with size and position validation,
area calculation, and custom string representation.
"""


class Square:
    """
    Defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The side length of the square.
            position (tuple): The coordinates of the square (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the private __size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size with validation.

        Args:
            value (int): The new size.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the private __position attribute."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position with validation.

        Args:
            value (tuple): A tuple of 2 positive integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the current square area.

        Returns:
            The area (size squared).
        """
        return self.__size ** 2

    def __str__(self):
        """
        Defines the string representation of the Square for printing.

        Returns:
            A string of the square using the # character and position.
        """
        if self.__size == 0:
            return ""

        output = []

        # Vertical offset (newlines based on y coordinate)
        for _ in range(self.__position[1]):
            output.append("")

        # Square rows
        for _ in range(self.__size):
            # Horizontal offset (spaces based on x coordinate)
            row = (" " * self.__position[0]) + ("#" * self.__size)
            output.append(row)

        return "\n".join(output)

    def my_print(self):
        """Prints the square to stdout using position and size."""
        print(self.__str__())
