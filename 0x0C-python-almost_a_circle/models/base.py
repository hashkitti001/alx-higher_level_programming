#!/usr/bin/python3

class Base:
    """
    Defines a class Base which would be the parent class for other classes in the directory
    Args: 
         id(int): 
    """
    __nb_objects = 0
    def __init__(self, id=None):
        if self.id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    
