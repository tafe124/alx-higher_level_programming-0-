#!/usr/bin/python3
""" Module for adding new attribute to an object """


def add_attribute(obj, name, value):
    """ Function that adds new attribute to an object """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
