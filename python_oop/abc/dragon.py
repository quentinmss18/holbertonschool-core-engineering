#!/usr/bin/env python3
"""
This module demonstrates the use of Mixins to compose 
behaviors in a Dragon class.
"""


class SwimMixin:
    """Mixin to provide swimming functionality."""

    def swim(self):
        """Prints the swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin to provide flying functionality."""

    def fly(self):
        """Prints the flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    A Dragon class that inherits capabilities from SwimMixin and FlyMixin,
    demonstrating composition through multiple inheritance.
    """

    def roar(self):
        """Prints the dragon's unique behavior."""
        print("The dragon roars!")
