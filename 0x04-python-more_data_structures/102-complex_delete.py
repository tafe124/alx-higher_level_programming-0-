#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        for key in list(a_dictionary):
            if a_dictionary[key] == value:
                del a_dictionary[key]
    return a_dictionary
