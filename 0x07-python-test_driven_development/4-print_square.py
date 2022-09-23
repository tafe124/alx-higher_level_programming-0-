#!/usr/bin/python3
"""
Module 4-print_square
prints a square with the character #
accepts the size
"""


def print_square(size):
    """
    Prints square with #
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end="")
    else:
        for row in range(size):
            print("#" * size)
