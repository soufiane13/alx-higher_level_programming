#!/usr/bin/python3
# 4-inherits_from.py
"""Defines an inherited check function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance from a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match .
    Returns:
        If obj is an inherited instance of a_class - True.
        Or - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
