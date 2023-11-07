#!/usr/bin/python3
# 3-is_kind_of_class.py
"""Defines a class and inherited check function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance from a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match .
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Or - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
