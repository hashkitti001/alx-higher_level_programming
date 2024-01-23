#!/usr/bin/python3
"""Defines a Square class"""
class Square:
    """Represents a square"""
    def __init__(self, size=0, position=(0,0)):
       """Initializes a new square
       Args:
           size (int): The size of the new square
       """
       if not isinstance(size, int):
            raise TypeError("size must be an integer")
       elif size < 0:
            raise ValueError("size must be >= 0")
       self.__size = size
       self.__position = position
    def area(self):
        """Returns the area of the square """
        return self.__size ** 2
    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size
    @size.setter
    def size(self, value):
        """Modifies the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def my_print(self):
        """Prints the square"""
        if(self.size is 0):
            print("")
        for i in range(self.size):
            print("#" * self.size)
    @property 
    def position(self):
        """Getter for the position private attribute"""
        return self.__position
    @position.setter
    def position(self, value):
        """Sets the position private attribute"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")