#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    sum = 0
    for elem in uniq_list:
        sum += elem
    return sum
