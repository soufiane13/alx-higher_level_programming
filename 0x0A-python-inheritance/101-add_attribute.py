#!/usr/bin/python3
# 101-add_attribute.py
"""Defines a function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object .

    Args:
        obj (any):  object to add an attribute to.
        att (str):  name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
