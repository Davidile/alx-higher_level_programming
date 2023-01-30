#!/usr/bin/python3

"""Module that holds the definition of a Square class."""


class Square:
    """Models a square."""

    def __init__(self, size=0):
        """Initialize a square object.

        Args:
            size (int): The size of the square object.
        """
        self.size = size

    @property
    def size(self):
        """Access the private attribute size.

        Perform checks on the object variable before
        assigning it to the private attribute size.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Compute the square area."""
        return self.size ** 2

    def __eq__(self, other):
        """Check the equality of the square area of two instances."""
        return self.area() == other.area()

    def __lt__(self, other):
        """Define the < comparison operator."""
        return self.area() < other.area()

    def __gt__(self, other):
        """Define the > comparison operator."""
        return self.area() > other.area()

    def __le__(self, other):
        """Define the <= comparison operator."""
        return self.area() <= other.area()

    def __ge__(self, other):
        """Define the >= comparison operator."""
        return self.area() >= other.area()

    def __ne__(self, other):
        """Define the != comparison operator."""
        return self.area() != other.area()
