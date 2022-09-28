#!/usr/bin/python3
""" Module for Pascal triangle problem """


def pascal_triangle(n):
    """ eturns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    lst = []
    if n <= 0:
        return lst
    lst.append([1])
    i = 0

    while i < n - 1:
        before = lst[i]
        row = []
        row.append(before[0])
        j = 0
        while j < (len(before) - 1):
            row.append((before[j] + before[j + 1]))
            j += 1
        row.append(before[j])
        lst.append(row)
        i += 1

    return lst
