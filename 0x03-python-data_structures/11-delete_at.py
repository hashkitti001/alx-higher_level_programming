#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if (my_list[idx] == -1 or my_list[idx] < 0):
        return my_list
    del my_list[idx]
    return my_list[idx]
