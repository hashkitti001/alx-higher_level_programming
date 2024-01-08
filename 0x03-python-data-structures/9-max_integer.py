#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is None:
        return None
    else:
        max_el = my_list[0]
        for i in range(len(my_list)):
            if (my_list[i] > max_el):
                max_el = my_list[i]
        return max_el
