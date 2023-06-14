#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniques = set(my_list)
    total = 0

    for i in uniques:
        total += i
    return total
