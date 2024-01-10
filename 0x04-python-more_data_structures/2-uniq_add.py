#!/usr/bin/python3
if __name__ == '__main__':
    def uniq_add(my_list=[]):
        sum = 0
        uniq_list = set(my_list)
        for elem in uniq_list:
            sum += elem
        return sum
