#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    pcount = 0
    for idx in range(x):
        try:
            print("{:d}".format(my_list[idx]), end="")
            pcount += 1
        except (TypeError, ValueError):
            continue
    print("")
    return pcount
