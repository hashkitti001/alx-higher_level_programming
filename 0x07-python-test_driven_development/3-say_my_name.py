#!/usr/bin/python3
"""Defines a program that prints a string"""
def say_my_name(first_name, last_name=""):
    """A function that prints a string with first_name and last_name interpolated into it"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    return "My name is {} {}".format(first_name, last_name)
