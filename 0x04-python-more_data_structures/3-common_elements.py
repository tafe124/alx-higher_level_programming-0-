#!/usr/bin/python3

def common_elements(set_1, set_2):
    if set_1 and set_2:
        common = {ele1 for ele1 in set_1 for ele2 in set_2 if ele1 == ele2}

        return common
    return {} 
