#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):
    """Represents a rectangle"""
    def __init__(self, width, height, x=0, y=0):
        """
        Constructor function to the Rectangle class

        Args: 
          __width(int):  represents the width of the Rectangle instance
          __height(int): represents the height of the Rectangle instance
          x(int): Represents the positional x-coordinate of the Rectangle instance
          y(int): Represents the positional y-coordinate of the Rectangle instance
          id(int): Identifier of the Rectangle
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init(id)
        
        @property
        def get_width(self):
            """Gets the width of the rectangle"""
            return self.__width
        @width.setter
        def set_width(self, value):
            """Sets the width of the rectangle"""
            if(value is not isinstance(int)):
                raise TypeError("width must be an integer")
            if(value <= 0):
               raise ValueError("width must be > 0")
            self.width = value
        @property
        def get_height(self):
            """Gets the height of the rectangle"""
            return self.__height
        
        @width.setter
        def set_height(self, value):
            """Sets the width of the rectangle"""
            if(value is not isinstance(int)):
                raise Exception("height must be an integer")
            if(value <= 0):
               raise Exception("height must be > 0")
            self.height = value
        @property
        def get_x(self):
            """Gets the positional x coordinate of the rectangle"""
            return self.__x
        @x.setter
        def set_x(self, value):
            """Sets the positional x coordinate to a value of 'value'"""
            if(value is not isinstance(int)):
                raise Exception("x must be an integer")
            if(value <= 0):
               raise Exception("x must be > 0")
            self.x = value
        @property
        def get_y(self):
            """Gets the positional y coordinate of the rectangle"""
            return self.__y
        @x.setter
        def set_y(self, value):
            """Sets the positional y coordinate to a value of 'value'"""
            if(value is not isinstance(int)):
                raise Exception("x must be an integer")
            if(value <= 0):
               raise Exception("x must be > 0")
            self.height = value