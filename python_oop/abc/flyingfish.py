#!/usr/bin/env python3
"""
This module explores multiple inheritance through the FlyingFish class,
which inherits from both Fish and Bird.
"""


class Fish:
    """Class representing a fish."""

    def swim(self):
        """Prints the fish's swimming action."""
        print("The fish is swimming")

    def habitat(self):
        """Prints the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """Class representing a bird."""

    def fly(self):
        """Prints the bird's flying action."""
        print("The bird is flying")

    def habitat(self):
        """Prints the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a FlyingFish, inheriting from both Fish and Bird.
    Demonstrates multiple inheritance and method overriding.
    """

    def fly(self):
        """Overrides Bird's fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Overrides Fish's swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Overrides both Fish and Bird's habitat methods."""
        print("The flying fish lives both in water and the sky!")
