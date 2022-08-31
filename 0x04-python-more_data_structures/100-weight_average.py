#!/usr/bin/python3
def weight_average(my_list=[]):
    weight_average = 0

    if my_list:
        total_score = 0
        total_weight = 0
        for score, weight in my_list:
            total_score += score * weight
            total_weight += weight

        weight_average = total_score / total_weight

    return weight_average
