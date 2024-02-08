#!/usr/bin/python3
from base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor function for the Rectangle class

        Args: 
          width (int): represents the width of the Rectangle instance
          height (int): represents the height of the Rectangle instance
          x (int): Represents the positional x-coordinate of the Rectangle instance
          y (int): Represents the positional y-coordinate of the Rectangle instance
          id (int): Identifier of the Rectangle
          Raises: 
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @property
    def x(self):
        """Gets the positional x coordinate of the rectangle"""
        return self.__x

    @property
    def y(self):
        """Gets the positional y coordinate of the rectangle"""
        return self.__y

    @property
    def width(self):
        """Gets the width of the rectangle"""
        return self.__width

    @width.setter
    def set_width(self, value):
        """Sets the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle"""
        return self.__height

    @height.setter
    def set_height(self, value):
        """Sets the width of the rectangle"""
        if type(value) != int:
            raise Exception("height must be an integer")
        if (value <= 0):
            raise Exception("height must be >= 0")
        self.__height = value
    
    @property
    def x(self):
        """Gets the positional x coordinate of the rectangle"""
        return self.__x

    @x.setter
    def set_x(self, value):
        """Sets the positional x coordinate to a value of 'value'"""
        if type(value) != int:
            raise Exception("x must be an integer")
        if (value <= 0):
            raise Exception("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Gets the positional y coordinate of the rectangle"""
        return self.__y

    @y.setter
    def set_y(self, value):
        """Sets the positional y coordinate to a value of 'value'"""
        if type(value) != int:
            raise Exception("y must be an integer")
        if (value <= 0):
            raise Exception("y must be >= 0")
        self.__y = value
    def area(self):
        """Returns the area of the Rectangle"""
        return self.width * self.height
    def display(self):
            """Print the Rectangle using the `#` character."""
            if self.width == 0 or self.height == 0:
                print("")
                return

            [print("") for y in range(self.y)]
            for h in range(self.height):
                [print(" ", end="") for x in range(self.x)]
                [print("#", end="") for w in range(self.width)]
                print("")
    def __str__(self):
        """Returns a string representation of the properties of the Rectangle object"""
        return f"[Rectangle] ({self.id}) {self.x}/ {self.y} - {self.width}/ {self.height}"
