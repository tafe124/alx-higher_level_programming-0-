#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        sorted_dict = sorted([(k, v) for k, v in a_dictionary.items()])

        for key, value in sorted_dict:
            print("{}: {}".format(key, value))
