#!/usr/bin/python3
"""Defines a class MyList that inherits the properties from a class list"""
class MyList(list):
    """Implements sorted printing for the built-in class list"""
    def print_sorted(self):
        print(sorted(self))