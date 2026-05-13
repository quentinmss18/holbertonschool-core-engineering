#!/usr/bin/env python3
"""
This module demonstrates Abstract Base Classes and Duck Typing
using geometric shapes.
"""
import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Returns the area of the circle: π * r^2."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Returns the circumference of the circle: 2 * π * r."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Returns the area of the rectangle: width * height."""
        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of the rectangle: 2 * (width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape.
    Uses Duck Typing: as long as 'shape' has area() and perimeter()
    methods, this function will work regardless of the object's class.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
