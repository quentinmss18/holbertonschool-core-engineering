#!/usr/bin/env python3
"""
Module defining the BaseGeometry class.
"""


class BaseGeometry:
    """A foundational class for geometric shapes."""

    def area(self):
        """
        Calculates the area of the shape.

        Raises:
            Exception: If the area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (any): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
