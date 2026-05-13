#!/usr/bin/env python3
"""
This module defines the VerboseList class which extends the built-in 
list class to provide notifications on item modifications.
"""


class VerboseList(list):
    """
    A list subclass that prints messages when items are added or removed.
    """

    def append(self, item):
        """Adds an item and prints a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        """Extends the list and prints the number of items added."""
        num_items = len(x)
        super().extend(x)
        print(f"Extended the list with [{num_items}] items.")

    def remove(self, item):
        """Prints notification before removing an item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Prints notification before popping an item.
        Defaults to the last item if index is not provided.
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
