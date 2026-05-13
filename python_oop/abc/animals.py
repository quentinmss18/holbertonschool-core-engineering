#!/usr/bin/env python3
"""
This module defines an abstract base class Animal and its 
concrete subclasses Dog and Cat.
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class representing a generic animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that must be implemented by subclasses."""
        pass


class Dog(Animal):
    """Subclass of Animal representing a dog."""

    def sound(self):
        """Returns the specific sound of a dog."""
        return "Bark"


class Cat(Animal):
    """Subclass of Animal representing a cat."""

    def sound(self):
        """Returns the specific sound of a cat."""
        return "Meow"
