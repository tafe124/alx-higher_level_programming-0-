#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    diff = set()
    if isinstance(set_1, set) and isinstance(set_2, set):
        diff = (set_1 - set_2) | (set_2 - set_1)

    return diff
