#!/usr/bin/python3
"""A function that checks for lowercase characters"""


def islower(c):
    if (ord(c) >= 97 and ord(c) <= 122):
        return True
    return False
