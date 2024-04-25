#!/usr/bin/python3
# A function that finds a peak in a list of unsorted integers.
def find_peak(list_of_integers):
    arrlen = len(list_of_integers)
    #Sort the list with insertion sort 
    for i in range(1, arrlen):
        curr = list_of_integers[i]
        while (list_of_integers[i - 1] > curr and i > 0):
            list_of_integers[i], list_of_integers[i - 1] = list_of_integers[i - 1], list_of_integers[i]
            i -= 1
    #Return the last one since the last one in sorted lexicographic order is the peak
    result = None if arrlen == 0 else list_of_integers[arrlen - 1]
    return result
