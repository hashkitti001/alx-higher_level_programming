#!/usr/bin/python3

class Base:
    """
    Defines a class Base which would be the parent class for other classes in the directory
    Private variables:
    __nb_objects(int): The number of objects created from the Base class
    Args: 
         id(int): Identifier of the object instance
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializes a new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    
