#!/usr/bin/env python3
"""
Module defining the Square class that inherits from Rectangle.
"""
Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The width and height of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
