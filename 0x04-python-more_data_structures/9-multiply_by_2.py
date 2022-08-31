#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = {}
    if a_dictionary is not None:
        for key in list(a_dictionary):
            new_dict[key] = a_dictionary[key] * 2

    return new_dict
