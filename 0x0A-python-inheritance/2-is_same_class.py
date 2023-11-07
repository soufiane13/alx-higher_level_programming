#!/usr/bin/python3
# 2-is_same_class.py
"""Defines a class that checks function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match.
    Returns:
        If obj is exactly an instance of a_class - True.
        Or - False.
    """
    if type(obj) == a_class:
        return True
    return False
