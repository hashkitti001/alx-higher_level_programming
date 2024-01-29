#!/usr/bin/python3
"""Defines an integer addition functions"""
def add_integer(a, b=98):
    """Returns the sum of a and b
    Args: 
       a (int): The first number 
       b (int): The second number with a default value of 98
    """
    if not isinstance(a, int or float):
       raise TypeError("a must be an integer")
    elif not isinstance(b, int or float):
       raise TypeError("b must be an integer")
    return int(a) + (b)
