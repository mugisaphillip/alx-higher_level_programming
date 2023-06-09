#!/usr/bin/python3
"""This module defines a Rectangle Class"""


class Rectangle:
    """A class called Rectangle

    Attributes:
    attr1(width): width of rectangle
    attr2(height): height of rectangle
    attr3(number_of_instances): number of instances
    attr4(print_symbol): symbol for representation
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the class instance"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the class instance"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the class instance"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the class instance"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the class instance"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the permimeter of the class instance"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Returns the string representation of the class instance"""
        strrep = ""
        if self.__width == 0 or self.__height == 0:
            return strrep
        for row in range(self.__height):
            for column in range(self.__width):
                strrep += str(self.print_symbol)
            if row < self.__height - 1:
                strrep += "\n"
        return strrep

    def __repr__(self):
        """Returns the string representation of the class
        instance for recreation"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Finalizer when instance is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
