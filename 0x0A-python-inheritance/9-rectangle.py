#!/usr/bin/python3
# 9-rectangle.py
"""Defines a class Rectangle that inherits from BaseGeometryclass."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle using BaseGeometry class."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width .
            height (int): The height .
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """ the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """ the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
