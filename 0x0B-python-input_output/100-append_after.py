#!/usr/bin/python3
# 100-append_after.py

""" It Defines a text file insertion ."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing in a file.

    Args:
        filename (str): The name .
        search_string (str): The string to search .
        new_string (str): The string to insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
