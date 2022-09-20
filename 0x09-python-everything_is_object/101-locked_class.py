#!/usr/bin/python3
"""
A module that containts a clas that avoids
dynmaically created attributes
"""


class LockedClass:
    """ Locked class """
    __slots__ = ['first_name']

    def __init__(self):
        """ Init method """
        pass
