#!/usr/bin/python3

def best_score(a_dictionary):
    top_score = None
    if a_dictionary:
        top_score = sorted([(v, k)
                            for k, v in a_dictionary.items()], reverse=True)
        top_score = top_score[0][1]

    return top_score
