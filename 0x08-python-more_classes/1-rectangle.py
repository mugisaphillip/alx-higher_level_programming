#!/usr/bin/python3
"""This module defines a Rectangle Class"""


class Rectangle:
    """A class called Rectangle

    Attributes:
    attr1(width): width of rectangle
    attr2(height): height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @width
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

    @height
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
